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
        for j in range(3) if board[i][j]
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
    for i in range(3):
        if board[i] == [X] * 3:
            return X
        elif board[i] == [O] * 3:
            return O
    for j in range(3):
        col = [board[i][j] for i in range(3)]
        if col == [X] * 3:
            return X
        elif col == [O] * 3:
            return O
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
        
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


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
