"""
Handles all the client connections, creating new games and requests from the client(s).
"""

import socket
import threading
import time
from player import Player
from game import Game
import json


class Server:
    PLAYERS = 4

    def __init__(self):
        self.connection_queue = []
        self.game_id = 0

    def player_thread(self, conn, player):
        """
        handles in  game communication between clients
        :param conn: connection object
        :param ip: str
        :param name: str
        :return: None
        """
        while True:
            try:
                # Receive request
                try:
                    data = conn.recv(1024)
                    data = json.loads(data.decode())
                except Exception as e:
                    break
                # Player is not a part of a game
                keys = [int(key) for key in data.keys()]
                send_msg = {key: [] for key in keys}
                last_board = None
                for key in keys:
                    if key == -1:  # get game - returns a list of players
                        if player.game:
                            send = {player.get_name(): player.get_score() for player in player.game.players}
                            send_msg[-1] = send
                        else:
                            send_msg[-1] = []
                    if player.game:
                        if key == 0:  # guess
                            correct = player.game.player_guess(player, data['0'][0])
                            send_msg[0] = correct

                        elif key == 1:  # skip
                            skip = player.game.skip(player)
                            send_msg[1] = skip

                        elif key == 2:  # get chat
                            content = player.game.round.chat.get_chat()
                            send_msg[2] = content

                        elif key == 3:  # get  board
                            brd = player.game.board.get_board()
                            if last_board != brd:
                                last_board = brd
                                send_msg[3] = brd



                        elif key == 4:  # get score
                            scores = player.game.get_player_scores()
                            send_msg[4] = scores
                        elif key == 5:  # get round
                            rnd = player.game.round_count
                            send_msg[5] = rnd
                        elif key == 6:  # get word
                            word = player.game.round.word
                            send_msg[6] = word

                        elif key == 7:  # get skips
                            skips = player.game.round.skips
                            send_msg[7] = skips

                        elif key == 8:  # update board
                            if player.game.round.player_drawing == player:
                                x, y, color = data['8'][:3]
                                player.game.update_board(x, y, color)
                        elif key == 9:  # get round time
                            t = player.game.round.time
                            send_msg[9] = t

                        elif key == 10:  # clear board
                            player.game.board.clear()

                        elif key == 11:
                            send_msg[11] = player.game.round.player_drawing == player

                    # if key == 10:  # disconnect received from client
                    #     raise Exception("Not a valid request")

                conn.sendall(json.dumps(send_msg).encode())
                conn.sendall(".".encode())

            except Exception as e:
                print(f"[EXCEPTION] {player.get_name()}:", e)
                break

        print(f"[DISCONNECT] {player.name} DISCONNECTED")
        if player.game:
            player.game.player_disconnected(player)
        conn.close()

    def handle_queue(self, player):
        """
        Adds player to queue and creates new game if enough players on board
        :param player:
        :return:
        """
        self.connection_queue.append(player)
        if len(self.connection_queue) >= self.PLAYERS:
            game = Game(self.game_id, self.connection_queue[:])

            for p in self.connection_queue:
                p.set_game(game)

            self.game_id += 1
            self.connection_queue = []

    def authentication(self, conn, addr):
        """
        authentication  here
        :param ip:
        :return:
        """
        try:
            data = conn.recv(1024)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")

            conn.sendall("1".encode())
            player = Player(addr, name)
            self.handle_queue(player)
            thread = threading.Thread(target=self.player_thread, args=(conn, player))
            thread.start()

        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()

    def connection_thread(self):
        server = "localhost"
        port = 5555

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen(2)
        print("Waiting for a connection, Server started")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection!", addr)

            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
