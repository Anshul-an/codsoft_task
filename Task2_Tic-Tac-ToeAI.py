# Task 2 - Tic-Tac-Toe AI using Minimax Algorithm


import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        print(" " + board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])
        if i < 2:
            print("---|---|---")
    print()

# Check for winner
def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for condition in win_conditions:
        if brd[condition[0]] == brd[condition[1]] == brd[condition[2]] == player:
            return True
    return False

# Check for draw
def is_draw(brd):
    return ' ' not in brd

# Get empty positions
def get_available_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    elif is_winner(brd, 'X'):
        return -1
    elif is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(best_score, score)
        return best_score

# AI move using minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

# Player move
def player_move():
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Choose a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O. Let's begin!")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(board, 'X'):
            print("🎉 You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print("AI's move...")
        ai_move()
        print_board()
        if is_winner(board, 'O'):
            print("🤖 AI wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
