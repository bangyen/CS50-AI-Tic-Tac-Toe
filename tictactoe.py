"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY] * 3 for _ in range(3)]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = sum(sum(map(bool, row)) for row in board)
    
    return [X, O][count % 2]
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {
        (i, j) for i in range(3)
        for j in range(3) if not board[i][j]
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)
    
    return b2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    trans = [board[i][j] for j in range(3) for i in range(3)]
    win_list = [[X] * 3, [O] * 3]
    
    for i in range(3):
        if board[i] in win_list:
            board[i][0]
    for j in range(3):
        if trans[j] in win_list:
            return trans[j][0]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O]:
        return True
    
    return all(all(row) for row in board)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return (winner(board) == X) - (winner(board) == O)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];
