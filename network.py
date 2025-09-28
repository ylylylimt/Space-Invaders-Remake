import socket
import pickle
import threading


class Network:
    def __init__(self, game_id):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.local_ip = "192.168.0.15"
        self.port = 5555
        self.addr = (self.local_ip, self.port)
        self.client.bind(("", 0))
        self.p = None
        self.running = True
        self.lock = threading.Lock()
        self.game_id = game_id

        self.listen_thread = threading.Thread(target=self.listen)
        self.listen_thread.start()
        self.connect()

    def connect(self):
        try:
            self.send("connect" + str(self.game_id))
            while self.p is None:
                pass
        except:
            pass

    def send(self, data):
        try:
            self.client.sendto(pickle.dumps(data), self.addr)
        except socket.error as e:
            print(e)

    def listen(self):
        while self.running:
            try:
                data, addr = self.client.recvfrom(2048)
                with self.lock:
                    self.p = pickle.loads(data)
            except socket.error as e:
                print(e)

    def getP(self):
        with self.lock:
            return self.p

    def close(self):
        self.running = False
        self.listen_thread.join()
        self.client.close()