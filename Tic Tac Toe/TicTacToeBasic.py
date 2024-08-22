import numpy as np
import random
from time import sleep


def empty_board():
    board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    return board


def empty_places(board):
    I = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                I.append((i, j))
    return I


def random_place(board, player):
    select = empty_places(board)
    current_location = random.choice(select)
    board[current_location] = player
    return board


def row_winner(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win:
            return True
    return False


def col_winner(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                continue

        if win:
            return True
    return False


def diag_winner(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False

    if win:
        return True

    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False

    return win


def evaluate_game(board):
    winner = 0
    for player in [1, 2]:
        if (
            row_winner(board, player)
            or col_winner(board, player)
            or diag_winner(board, player)
        ):

            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


def tic_tac_toe():
    board = empty_board()
    winner = 0
    counter = 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            brd = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(brd)
            sleep(5)
            counter += 1
            winner = evaluate_game(brd)

            if winner != 0:
                break
    return winner


print("Winner is player: " + str(tic_tac_toe()))
