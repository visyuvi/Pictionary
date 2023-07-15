from board import Board
from round import Round
import random


class Game:

    def __init__(self, id, players):
        """
        initialize the game! once player threshold is met
        :param id: int
        :param players: Players[]
        """
        self.id = id
        self.players = players
        self.words_used = set()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.round_count = 1
        self.start_new_round()

    def start_new_round(self):
        """
        Starts a new round with a new word
        :return:  None
        """
        round_word = self.get_word()
        self.round = Round(round_word, self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1
        self.round_count += 1
        if self.player_draw_ind >= len(self.players):
            self.round.end_round("")
            self.end_game()


    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return:
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player:
        :raises Exception
        :return:
        """

        # todo check this
        if player in self.players:
            player_ind = self.players.index(player)
            if player_ind > self.player_draw_ind:
                self.player_draw_ind -= 1
            self.players.remove(player)
            self.round.player_left(player)
        else:
            raise Exception("Player not in game")

        if len(self.players) <= 2:
            self.end_game()

    def get_player_scores(self):
        """
        give a dict of player scores
        :return: dict
        """
        scores = {player: player.get_score() for player in self.players}
        return scores

    def skip(self):
        """
        Increments the round skips, if skips are greater than threshold, starts new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet")

    def round_ended(self):
        """
        If the round ends call this
        :return: None
        """
        self.start_new_round()
        self.board.clear()

    def update_board(self, x, y, color):
        """
        calls update method on board
        :param x: int
        :param y: int
        :param color: (int, int, int)
        :return: None
        """
        if not self.board:
            raise Exception("No board created")
        self.board.update(x, y, color)

    def end_game(self):
        """
        ends the game
        :return:
        """
        # TODO implement
        for player in self.players:
            self.round.player_left(player)

    def get_word(self):
        """
        gives a word that has not been used
        :return: str
        """
        with open('words.txt') as f:
            words = []
            for line in f:
                wrd = line.strip()
                if wrd not in self.words_used:
                    words.append(wrd)

        r = random.randint(0, len(words) - 1)
        wrd = words[r].strip()
        self.words_used.add(wrd)

        return words[r].strip()
