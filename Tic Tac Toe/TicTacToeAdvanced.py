import numpy as np
import random


def empty_board():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])


def print_board(board):
    symbols = {0: "-", 1: "X", 2: "O"}
    print("\nBoard:")
    for row in board:
        print(" | ".join([symbols[cell] for cell in row]))
    print()


def empty_places(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]


def player_move(board, player):
    while True:
        move = input(
            f"Player {player}, enter your move (row and column numbers 1-3 separated by a space): "
        ).split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers.")
            continue
        try:
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if (row, col) in empty_places(board):
                board[row, col] = player
                break
            else:
                print("Invalid move. The cell is already occupied or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def random_place(board, player):
    current_location = random.choice(empty_places(board))
    board[current_location] = player


def check_winner(board, player):
    for i in range(3):
        if all([board[i, j] == player for j in range(3)]) or all(
            [board[j, i] == player for j in range(3)]
        ):
            return True
    if all([board[i, i] == player for i in range(3)]) or all(
        [board[i, 2 - i] == player for i in range(3)]
    ):
        return True
    return False


def evaluate_game(board):
    for player in [1, 2]:
        if check_winner(board, player):
            return player
    if not empty_places(board):
        return -1
    return 0


def tic_tac_toe():
    board = empty_board()
    print_board(board)
    winner = 0

    while winner == 0:
        player_move(board, 1)
        print_board(board)
        winner = evaluate_game(board)
        if winner != 0:
            break

        print("Computer's move...")
        random_place(board, 2)
        print_board(board)
        winner = evaluate_game(board)

    if winner == -1:
        print("The game is a draw!")
    else:
        print(f"Winner is player {winner}!")


tic_tac_toe()
