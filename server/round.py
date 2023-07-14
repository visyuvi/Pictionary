import time as t
from _thread import start_new_thread


class Round:
    def __init__(self, word, player_drawing, players):
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
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        start_new_thread(self.time_thread, ())

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
        : returns bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TO DO implement scoring system here

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
        # TODO implement end_round functionality
        pass

