import pygame
from button import Button, TextButton
from board import Board
from top_bar import TopBar
from main_menu import MainMenu
from chat import Chat
from leaderboard import Leaderboard
from player import Player
from bottom_bar import BottomBar


class Game:
    BG = (255, 255, 255)

    def __init__(self):
        self.WIDTH = 1300
        self.HEIGHT = 1000
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.leaderboard = Leaderboard(50, 122.5)
        self.board = Board(305, 125)
        self.top_bar = TopBar(10, 10, self.WIDTH - 20, 100)
        self.top_bar.change_round(1)
        self.players = [Player("Vishal"), Player("Prakrati"), Player("Karan"), Player("Tripti"), Player("Surabhi")]
        self.skip_button = TextButton(85, 810, 100, 50, (255, 255, 0), "Skip")
        self.bottom_bar = BottomBar(305, 860, self)
        self.chat = Chat(1030, 121)
        self.draw_color = 1
        for player in self.players:
            self.leaderboard.add_player(player)

    def draw(self):
        self.win.fill(self.BG)
        self.leaderboard.draw(self.win)
        self.top_bar.draw(self.win)
        self.board.draw(self.win)
        self.skip_button.draw(self.win)
        self.bottom_bar.draw(self.win)
        self.chat.draw(self.win)
        pygame.display.update()

    def check_clicks(self):
        """
        handles clicks on buttons and screen
        :return: None
        """

        mouse = pygame.mouse.get_pos()

        # Check click on skip button
        if self.skip_button.click(*mouse):
            print("Clicked skip button")

        clicked_board = self.board.click(*mouse)
        if clicked_board:
            self.board.update(*clicked_board, self.draw_color)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    self.bottom_bar.button_events()


        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    g = Game()
    g.run()