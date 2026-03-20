import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Function to display the board
def display_board(board):
    print()

    # Loop through rows (0,3,6)
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        
        # Print separator except last row
        if i < 6:
            print("--+---+--")

    print()


# Function to check winner
def check_winner(board, player):

    # All winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check each combination
    for condition in win_combinations:
        if (board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player):
            return True

    return False


# Check if board is full
def is_full(board):
    return " " not in board


# Player move function
def player_move(board):
    while True:
        try:
            # Take input and convert to index
            move = int(input(Fore.GREEN + "Enter a number (1-9): ")) - 1

            # Check valid range
            if move < 0 or move > 8:
                print(Fore.RED + "Enter a number between 1 and 9.")
                continue

            # Check if space is empty
            if board[move] == " ":
                board[move] = "X"   # FIXED HERE
                break
            else:
                print(Fore.RED + "That space is already taken. Try again.")

        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number.")


# Computer move (basic AI)
def computer_move(board):
    print(Fore.YELLOW + "Computer is making a move...")

    # Step 1: Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                return
            board[i] = " "

    # Step 2: Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                return
            board[i] = " "

    # Step 3: Random move
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"


# Main game loop
def play_game():
    board = [" "] * 9

    print(Fore.CYAN + "Welcome to Tic Tac Toe!")
    print("You are X and the computer is O.")

    while True:
        display_board(board)

        # Player turn
        player_move(board)

        if check_winner(board, "X"):
            display_board(board)
            print(Fore.GREEN + "You win!")
            break

        if is_full(board):
            display_board(board)
            print(Fore.YELLOW + "It's a tie!")
            break

        # Computer turn
        computer_move(board)

        if check_winner(board, "O"):
            display_board(board)
            print(Fore.RED + "Computer wins!")
            break

        if is_full(board):
            display_board(board)
            print(Fore.YELLOW + "It's a tie!")
            break


# Start game
play_game()