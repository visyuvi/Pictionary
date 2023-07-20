"""
Represents the chat for the game
"""
import pygame


class Chat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 225

        self.HEIGHT = 800
        self.BORDER_THICKNESS = 5
        self.content = []
        self.typing = ""
        self.chat_font = pygame.font.SysFont("comicsans", 20)
        self.type_font = pygame.font.SysFont("comicsans", 22)

        self.CHAT_GAP = 20

    def update_chat(self):
        self.content.append(self.typing)

    def draw(self, win):

        pygame.draw.rect(win, (200, 200, 220), (self.x, self.y + self.HEIGHT - 40, self.WIDTH, 40))
        pygame.draw.line(win, (0, 0, 0), (self.x, self.y + self.HEIGHT - 40),
                         (self.x + self.WIDTH, self.y + self.HEIGHT - 40), self.BORDER_THICKNESS)
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.WIDTH, self.HEIGHT), self.BORDER_THICKNESS)

        while len(self.content) * self.CHAT_GAP > self.HEIGHT - 60:
            self.content = self.content[: -1]

        for i, chat in enumerate(self.content):
            txt = self.chat_font.render(" - " + chat, 1, (0, 0, 0))
            win.blit(txt, (self.x + 15, 10 + self.y + i * self.CHAT_GAP))

        type_chat = self.type_font.render(self.typing, 1, (0, 0, 0))
        win.blit(type_chat, (self.x + 5, self.y + self.HEIGHT - 20 - type_chat.get_height() / 2))

    def type(self, char):
        if char == "BACKSPACE":
            if len(self.typing) > 0:
                self.typing = self.typing[:-1]
        elif char == "SPACE":
            self.typing += " "
        elif len(char) == 1:
            self.typing += char

        if len(self.typing) >= 19:
            self.typing = self.typing[:19]