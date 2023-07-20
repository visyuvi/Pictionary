import socket
import json
from time import sleep


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server = "127.0.0.1"  # Put server IP here
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name
        print(self.connect())

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            print(e)
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())

            d = ""
            last = 1
            while 1:
                last = self.client.recv(1024).decode()
                try:
                    if last == ".":
                        break
                except:
                    break
                d += last
            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server:", msg)
        self.client.close()


