def terminal_test(gameState):
    """ Return True if the game is over the active player and False otherwise.
    """
    return not bool(gameState.get_legal_move())

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child nodes.
    """
    if terminal_test(gameState):
        return 1
    v = float("inf")
    for m in gameState.get_legal_moves():
        v = min(v, max_value(gameState.forecast_move(m)))
    return v

def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child nodes.
    """
    if terminal_test(gameState):
        return -1
    v = float("-inf")
    for m in gameState.get_legal_moves():
        v = max(v, min_value(gameState.forecast_move(m)))
    return v
