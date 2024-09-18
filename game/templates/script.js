// Load environment variables
const API_URL = process.env.API_URL || 'http://localhost:8000/api/';

let currentPlayer = 'X';
let board = ['', '', '', '', '', '', '', '', ''];
let gameOver = false;
let boardId = null;

async function createGame() {
    const response = await fetch(`${API_URL}create_game/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            player1: { email: 'player1@example.com' },
            player2: { email: 'player2@example.com' },
        }),
    });
    const data = await response.json();
    boardId = data.board_id;
    console.log('Game created with board ID:', boardId);
}

async function updateBoard(i, j) {
    const response = await fetch(`${API_URL}update_board/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            board_id: boardId,
            i: i,
            j: j,
            user: currentPlayer,
        }),
    });
    const data = await response.json();
    return data;
}

async function getLatestState() {
    const response = await fetch(`${API_URL}get_latest_state/${boardId}/`);
    const data = await response.json();
    return data.data;
}

function createBoard() {
    const boardElement = document.getElementById('board');
    boardElement.innerHTML = '';
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.index = i;
        cell.addEventListener('click', handleCellClick);
        boardElement.appendChild(cell);
    }
}

async function handleCellClick(event) {
    const index = event.target.dataset.index;
    const i = Math.floor(index / 3);
    const j = index % 3;

    if (board[index] === '' && !gameOver) {
        const response = await updateBoard(i, j);
        if (response.status === 'continue') {
            board[index] = currentPlayer;
            event.target.textContent = currentPlayer;
            togglePlayer();
        } else if (response.status === 'win') {
            document.getElementById('status').textContent = `${currentPlayer} wins!`;
            gameOver = true;
        } else if (response.status === 'draw') {
            document.getElementById('status').textContent = 'Draw!';
            gameOver = true;
        }
    }
}

function togglePlayer() {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    document.getElementById('status').textContent = `Current Player: ${currentPlayer}`;
}

async function resetGame() {
    await createGame();
    board = ['', '', '', '', '', '', '', '', ''];
    gameOver = false;
    currentPlayer = 'X';
    document.getElementById('status').textContent = 'Current Player: X';
    createBoard();
}

document.getElementById('reset-btn').addEventListener('click', resetGame);

// Initialize the game
createGame().then(() => {
    createBoard();
});