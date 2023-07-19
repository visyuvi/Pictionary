"""
Represent the board object for the game
"""
# import random

import pygame


class Board:
    COLORS = {
        0: (255, 255, 255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 140, 0),
        7: (139, 69, 19),
        8: (128, 0, 128)
    }

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 720
        self.compressed_board = []
        self.BORDER_THICKNESS = 5
        self.DIVIDING_FACTOR = 8
        self.ROWS = self.HEIGHT / self.DIVIDING_FACTOR
        self.COLS = self.WIDTH / self.DIVIDING_FACTOR
        self.board = self.create_board()

    def create_board(self):
        # return [[self.COLORS[5] for _ in range(self.COLS)] for _ in range(self.ROWS)]

        return [[self.COLORS[0] for _ in range(int(self.COLS))] for _ in range(int(self.ROWS))]

    def translate_board(self):
        """
        Translate a compressed board into a regular board
        :return: None
        """
        for y, _ in enumerate(self.compressed_board):
            for x, col in enumerate(self.compressed_board[y]):
                self.board[y][x] = self.COLORS[col]

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x - self.BORDER_THICKNESS / 2, self.y - self.BORDER_THICKNESS / 2,
                                          self.WIDTH + self.BORDER_THICKNESS,
                                          self.HEIGHT + self.BORDER_THICKNESS),
                         self.BORDER_THICKNESS)
        for y, _ in enumerate(self.board):
            for x, col in enumerate(self.board[y]):
                pygame.draw.rect(win, col, (self.x + x * self.DIVIDING_FACTOR, self.y + y * self.DIVIDING_FACTOR,
                                            self.DIVIDING_FACTOR, self.DIVIDING_FACTOR), 0)

    def click(self, x, y):
        """
        None if not in board, otherwise return place clicked on
        in terms of row and col
        :param x: float
        :param y: float
        :return: (int, int) or None
        """
        row = int((x - self.x) / self.DIVIDING_FACTOR)
        col = int((y - self.y) / self.DIVIDING_FACTOR)

        if 0 <= row < self.ROWS and 0 <= col < self.COLS:
            return row, col
        return None

    def update(self, x, y, color, thickness=3):
        # TODO handle any thickness value
        neighs = [(x, y)] + self.get_neighbour(x, y)
        for x, y in neighs:
            if 0 <= x < self.COLS and 0 <= y < self.ROWS:
                self.board[y][x] = color

    def get_neighbour(self, x, y):
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x + 1, y - 1), (x, y + 1), (x + 1, y + 1)]

    def clear(self):
        self.board = self.create_board()
