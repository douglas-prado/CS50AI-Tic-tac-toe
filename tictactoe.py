"""
Tic Tac Toe Player
"""

import copy
import math
import random

X = "X"
O = "O"
EMPTY = None
maximum_value = 1
minimum_value = -1


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    blankspaces = 0

    for line in board:
        for value in line:
            if value == EMPTY:
                blankspaces = blankspaces + 1

    if (blankspaces % 2) == 0:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actual_line = 0
    possible_actions = set()

    for line in board:
        actual_column = 0
        for value in line:
            if value == EMPTY:
                possible_actions.add((actual_line, actual_column))
            actual_column += 1

        actual_line += 1

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if len(board) < action[0] or len(board[0]) < action[1]:
        raise RuntimeError ('This action is not possible')

    if board[action[0]][action[1]] != EMPTY:
        raise RuntimeError ('This action is not possible')

    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board [0][2] != EMPTY:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    if board[1][0] == board[1][1] == board[1][2] != EMPTY:
        if board[1][0] == X:
            return X
        elif board[1][0] == O:
            return O

    if board[2][0] == board[2][1] == board[2][2] != EMPTY:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O

    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    if board[0][1] == board[1][1] == board[2][1] != EMPTY:
        if board[0][1] == X:
            return X
        elif board[0][1] == O:
            return O

    if board[0][2] == board[1][2] == board[2][2] != EMPTY:
        if board[0][2] == X:
            return X
        elif board[0][2] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    if board[2][0] == board[1][1] == board[0][2] != EMPTY:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O or len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return maximum_value
    elif winner(board) == O:
        return minimum_value

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    """
    I made this implemantation just to have different starts when the player chooses O
    """

    list_actions = []

    for action in actions(board):
        list_actions.append(action)

    if len(list_actions) == 9:
        return list_actions[random.randrange(0, 9)]

    """
    I made this implemantation just to have different starts when the player chooses O
    """

    if player(board) == X:
        best_value = max_value(board)

        for action in actions(board):
            if best_value == min_value(result(board, action)):
                return action

    else:

        best_value = min_value(board)

        for action in actions(board):
            if best_value == max_value(result(board, action)):
                return action


def max_value(board):
    """
    Returns the maximum value for the board.
    """

    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == maximum_value:
            return maximum_value
    return v


def max(value_1, value_2):
    """
    Compares two values and returns the maximum value.
    """

    if value_1 > value_2:
        return value_1

    return value_2


def min_value(board):
    """
    Returns the minimum value for the board.
    """

    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == minimum_value:
            return minimum_value

    return v


def min(value_1, value_2):
    """
    Compares two values and returns the minimum value.
    """

    if value_1 < value_2:
        return value_1

    return value_2
