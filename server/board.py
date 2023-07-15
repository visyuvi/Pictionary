class Board:
    ROWS = COLS = 720

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
        :param color:
        :return:
        """
        self.data[y][x] = color

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
        return [(255, 255, 255) for _ in range(self.COLS) for _ in range(self.ROWS)]

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
