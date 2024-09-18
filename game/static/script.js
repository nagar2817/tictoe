let boardId;
let currentPlayerId;
let boardState;
let player1Id;
let player2Id;

function initializeGame() {
       const player1Email = document.getElementById('player1Email').value;
       const player2Email = document.getElementById('player2Email').value;

       fetch('/api/initialize-game/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({
               player1_email: player1Email,
               player2_email: player2Email
           })
       })
       .then(response => response.json())
       .then(data => {
           boardId = data.id;
           player1Id = data.player1;
           player2Id = data.player2;
           currentPlayerId = data.current_turn;
           boardState = data.board;
           document.getElementById('emailForm').style.display = 'none';
           document.getElementById('gameBoard').style.display = 'block';
           renderBoard();
       })
       .catch(error => console.error('Error:', error));
   }

function renderBoard() {
       const board = document.getElementById('board');
       board.innerHTML = '';
       for (let i = 0; i < 9; i++) {
           const cell = document.createElement('div');
           cell.className = 'cell';
           cell.textContent = boardState[i];
           cell.onclick = () => makeMove(i);
           board.appendChild(cell);
       }
       const currentPlayerSymbol = currentPlayerId === player1Id ? 'X' : 'O';
       document.getElementById('message').textContent = `Player ${currentPlayerSymbol}'s turn`;
   }

function makeMove(index) {
       const i = Math.floor(index / 3);
       const j = index % 3;

       fetch('/api/update-board/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({
               board_id: boardId,
               user_id: currentPlayerId,
               i: i,
               j: j
           })
       })
       .then(response => response.json())
       .then(data => {
           boardState = data.board;
           currentPlayerId = data.current_turn;
           renderBoard();
           checkGameStatus();
       })
       .catch(error => console.error('Error:', error));
   }

function checkGameStatus() {
       fetch(`/api/get-board-state/${boardId}/`)
       .then(response => response.json())
       .then(data => {
           boardState = data.board;
           if (checkWin(boardState)) {
               const winnerSymbol = data.current_turn === player1Id ? 'O' : 'X';
               document.getElementById('message').textContent = `Player ${winnerSymbol} wins!`;
               disableBoard();
           } else if (boardState.indexOf(' ') === -1) {
               document.getElementById('message').textContent = 'Draw!';
               disableBoard();
           }
       })
       .catch(error => console.error('Error:', error));
   }

function checkWin(board) {
       const winPatterns = [
           [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
           [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
           [0, 4, 8], [2, 4, 6]             // Diagonals
       ];
       for (let pattern of winPatterns) {
           if (board[pattern[0]] !== ' ' && board[pattern[0]] === board[pattern[1]] && board[pattern[1]] === board[pattern[2]]) {
               return true;
           }
       }
       return false;
   }

function disableBoard() {
       const cells = document.getElementsByClassName('cell');
       for (let cell of cells) {
           cell.onclick = null;
       }
   }

function resetGame() {
       document.getElementById('emailForm').style.display = 'block';
       document.getElementById('gameBoard').style.display = 'none';
       document.getElementById('player1Email').value = '';
       document.getElementById('player2Email').value = '';
   }