def check_winner(board, user):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == user:
            return True
    return False

def validMove(i, j, board):
    if i < 0 or i > 2 or j < 0 or j > 2:
        return False
        
    return True