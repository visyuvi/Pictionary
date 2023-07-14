from game import Game


class Player:
    def __init__(self, ip, name):
        """
        Initialize the player object
        :param ip: str
        :param name: str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        sets the player's game association
        :param game: Game
        :return: None 
        """
        self.game = game

    def update_score(self, x):
        """
        updates a player's score
        :param x: int
        :return: None
        """
        self.score += x

    def guess(self, wrd):
        """
        makes  a player guess
        :param wrd:
        :return: bool
        """
        return self.game.player_guess(self,  wrd)

    def disconnect(self):
        """
        call this to disconnect player
        :return:
        """
        pass

    def get_score(self):
        """
        Gets player score
        :return: int
        """
        return self.score

    def get_name(self):
        """
        Gets player name
        :return:
        """
        return self.name

    def get_ip(self):
        """
        gets player IP address
        :return:
        """
        return self.ip
