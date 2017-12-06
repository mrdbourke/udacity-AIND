# To code the minimax algorithm, first you'll implement a class to keep track
# of the game state for the mini-isolation game.
# The game state object will handle all of the rules of the game, and include
# all of the information describing the specific configuration of the game
# at a particular point in time.
# At a minimum, the board state needs to keep track of which cells are open
# and closed; which player has initiative (whose turn it is to move) and where
# each player is on the board.
from copy import deepcopy

xlim, ylim = 3, 2

class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1

    _parity: bool
        Keep track of active player initiative (which player has control to
        move) where 0 indicates that player one has initiative and 1 indicates
        player 2

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the board indices of their
        last move, e.g., [(0, 0), (1, 0)] means player 1 is at (0, 0) and player
        2 is at (1, 0)
    """

    def __init__(self):
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1 # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move applied to the
        current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_locations[self._parity] = move
        newBoard._parity ^= 1
        return newBoard

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the active player.
        Each player should get a list of all empty spaces on the board on their
        first move, and otherwise they should get a list of all open spaces in
        a straight line along any row, column or diagonal from their current
        position. (Players CANNOT move through obstacles or blocked squares.)
        Moves should be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        loc = self._player_locations[self._parity]
        if not loc:
            return self._get_black_spaces()
        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in rays:
            _x, _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]
                    break
                moves.append((_x, _y))
        return moves

    def _get_black_spaces(self):
        """ Return a list of blank spaces on the board."""
        return [(x, y) for y in range(ylim) for x in range(xlim)
            if self._board[x][y] == 0]


# Implementing the minimax algorithm.
# Assumption 1: a state is terminal if the active player has no remaining moves.
# Assumption 2: the board utility is -1 if it terminates at a max level,
# and +1 if it terminates at a min level.

""" This code is produced from the pseudocode in the AIMA textbook. """

def terminal_test(gameState):
    """ Return True if the game is over for the active player and False
    otherwise. """
    return not bool(gameState.get_legal_moves()) # by Assumption 1

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over, otherwise
    return the minimum value over all legal child nodes. """
    if terminal_test(gameState):
        return 1 # by Assumption 2
    v = float("inf")
    for m in gameState.get_legal_moves():
        v = min(v, max_value(gameState.forecast_move(m)))
    return v

def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over, otherwise
    return the maximum value over all legal child nodes. """
    if terminal_test(gameState):
        return -1 # by Assumption 2
    v = float("-inf")
    for m in gameState.get_legal_moves():
        v = max(v, max_value(gameState.get_legal_moves(m)))
    return v

""" The code above is created from the pseudocode in the AIMA textbook. """

# Bringing it all together to complete the minimax algorithm.
# The minimax() function should loop over all the legal moves from the current
# state and return the move that has the highest score according to the
# min_value() function.
# Min_value() is called first because the root node itself is a "max" node.

def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that has the best
    possible value. A move is a pair of coordinates in (column, row) order
    corresponding to a legal move for the searching player.

    You can ignore the special case of calling this fuction from a terminal
    state. """
    best_score = float("-inf")
    best_move = None
    for m in gameState.get_legal_moves():
        v = min_value(gameState.forecast_move(m))
        if v > best_score:
            best_score = v
            best_move = m
        return best_move
