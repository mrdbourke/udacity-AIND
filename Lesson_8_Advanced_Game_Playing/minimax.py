from minimax_helpers import *

# Solution using an explicit loop based on max_value()
def _minimax_decision(gameState):
    """ Return the move along a branch of the game tree that has the best
    possible value. A move is a pair of coordinates in (column, row) order
    corresponding to a legal move for the searching player.
    """
    best_score = float("-inf")
    best_move = None
    for m in gameState.get_legal_moves():
        v = min_value(gameState.forecast_move(m))
        if v > best_score:
            best_score = v
            best_move = m
        return best_move

# Another solution option. It does the same thing as the function above using
# the built-in 'max' function.
def minimax_decision(gameState):
    return max(gameState.get_legal_moves(),
                key = lambda m: min_value(gameState.forecast_move(m)))


#### Extra Note ####
""" The minimax algorithm implemented here will work on other games if you
enter the rules in the GameState class.
There are further optimizations which could be made to the algorithm such as
depth-limiting, alpha-beta pruning and iterative deepening that will allow
minimax to work on even larger games (checkers, chess, etc).
"""
