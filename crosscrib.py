import cribgui

#size constants
GRID_SIZE = 5

class CrossCribBoard:
    """
    CrossCrib board
    """

    def __init__(self, initialboard=None):
        self._board = [[None for idx in xrange(GRID_SIZE)]
                             for idx in xrange(GRID_SIZE)]

    def clone(self):
        """
        return copy of board
        """
        
        clone = [[self._board[row][col] for col in xrange(GRID_SIZE)]
                             for row in xrange(GRID_SIZE)]
        return clone

    def get_card(self, row, col):
        """
        get card at grid position
        """

        return self._board[row][col]

    def set_card(self, row, col, card):
        """
        set card at grid position
        """

        self._board[row][col] =  card
        