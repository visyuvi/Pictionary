import time as t
from _thread import start_new_thread
from game import Game
from chat import Chat


class Round:
    def __init__(self, word, player_drawing, players, game):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: []: contains Players
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.players = players
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.game = game
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Returns true if round skipped threshold met
        :return: bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            return True
        return False

    def get_scores(self):
        """
        :return: all the player scores
        """
        return self.player_scores

    def get_score(self, player):
        """
        Gets a specific players scores
        :param player: Player
        :return: int
        """
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("Player not in score list")

    def time_thread(self):
        """
        Runs in thread to keep track of time
        :return:
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TO DO implement scoring system here
            return correct

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        # might not be able to use player as key in dict
        if  player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing player left!")

    def end_round(self, msg):
        for player in self.players:
            player.update_score(self.player_scores[player])
        self.game.round_ended()
