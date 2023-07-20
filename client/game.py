import pygame
from button import TextButton
from board import Board
from top_bar import TopBar
from chat import Chat
from leaderboard import Leaderboard
from bottom_bar import BottomBar

pygame.init()


class Game:
    BG = (255, 255, 255)

    def __init__(self, win, connection=None):
        pygame.font.init()
        self.connection = connection
        self.win = win
        self.leaderboard = Leaderboard(50, 122.5)
        self.board = Board(305, 125)
        self.top_bar = TopBar(10, 10, 1280, 100)
        self.top_bar.change_round(1)
        self.players = []
        self.skip_button = TextButton(85, 810, 100, 50, (255, 255, 0), "Skip")
        self.bottom_bar = BottomBar(305, 860, self)
        self.chat = Chat(1030, 121)
        self.draw_color = 1

    def add_player(self, player):
        self.players.append(player)
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

            try:
                response = self.connection.send({3: []})
                self.board.compressed_board = response
                self.board.translate_board()
            except:
                run = False
                break

            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    self.check_clicks()
                    self.bottom_bar.button_events()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        self.chat.update_chat()
                        self.connection.send({0: [self.chat.typing]})
                        self.chat.typing = ""
                    else:
                        # gets the key name
                        key_name = pygame.key.name(event.key)

                        # converts it to uppercase
                        key_name = key_name.upper()
                        self.chat.type(key_name)

        pygame.quit()


# if __name__ == "__main__":
#     pygame.init()
#     g = Game(win)
#     g.run()
