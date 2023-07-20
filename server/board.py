class Board:
    ROWS = COLS = 90

    def __init__(self):
        """
        Initialize the board by creating empty board (all white pixels).
        """

        self.data = self._create_empty_board()

    def update(self, x, y, color):
        """
        Update a singular pixel of the board
        :param x:
        :param y:
        :param color: 0 - 8
        :return:
        """
        # TODO handle any thickness value
        # update neighbours
        neighs = [(x, y)] + self.get_neighbour(x, y)
        for x, y in neighs:
            if 0 <= x < self.COLS and 0 <= y < self.ROWS:
                self.data[y][x] = color

    """
    Function to get neighbours of x,y
    """
    def get_neighbour(self, x, y):
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x + 1, y - 1), (x, y + 1), (x + 1, y + 1)]

    def clear(self):
        """
        clears board to all white
        :return: None
        """
        self.data = self._create_empty_board()

    def _create_empty_board(self):
        """
        Creates an empty board
        :return: the created board
        """
        return [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def fill(self, x, y):
        """
         fills in a specific shape or area using recursion
        :param x: int
        :param y: int
        :return: None
        """
        pass

    def get_board(self):
        """
        Gets the data of the board.
        :return: (int, int, int)[]
        """
        return self.data
