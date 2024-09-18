## Features

- **Player Management**: Players are identified by their email addresses.
- **Game Initialization**: Start a new game by providing two player emails.
- **Game State Management**: Track the state of the game board and the current player's turn.
- **Win Detection**: Automatically detect when a player wins or when the game ends in a draw.
- **Reset Game**: Reset the game to play again.

## Usage

1. **Start the game**:
   - Open your browser and navigate to `https://tictoe-vcin.onrender.com/`.
   - Enter the email addresses of the two players and click "Start Game".

2. **Play the game**:
   - The game board will be displayed, and the current player's turn will be indicated.
   - Click on a cell to make a move.

3. **Check the game status**:
   - The game will automatically detect when a player wins or when the game ends in a draw.
   - The message will be updated accordingly.

4. **Reset the game**:
   - Click "Reset Game" to start a new game.

## API Endpoints

- **Initialize Game**:
  - **URL**: `/api/initialize-game/`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
      "player1_email": "player1@example.com",
      "player2_email": "player2@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "player1": 1,
      "player2": 2,
      "board": "         ",
      "current_turn": 1
    }
    ```

- **Update Board**:
  - **URL**: `/api/update-board/`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
      "board_id": 1,
      "user_id": 1,
      "i": 0,
      "j": 0
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "player1": 1,
      "player2": 2,
      "board": "X        ",
      "current_turn": 2
    }
    ```

- **Get Board State**:
  - **URL**: `/api/get-board-state/<board_id>/`
  - **Method**: `GET`
  - **Response**:
    ```json
    {
      "id": 1,
      "player1": 1,
      "player2": 2,
      "board": "X        ",
      "current_turn": 2
    }
    ```

- **Render HTML**:
  - **URL**: `/api/`
  - **Method**: `GET`
  - **Response**: HTML content of the game interface.