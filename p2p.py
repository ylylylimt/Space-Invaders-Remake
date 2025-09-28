import socket
import pickle
import threading
from player import Player

local_ip = "192.168.0.15"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((local_ip, port))

games = {
    0: [Player(200, 200, 50, 50, (54, 168, 73), 10, 720, 25), Player(700, 200, 50, 50, (221, 30, 38), 10, 45, 25)],
    1: [Player(700, 200, 50, 50, (255, 255, 0), 10, 45, 25), Player(200, 200, 50, 50, (0, 0, 255), 10, 720, 25)]
}
addresses = {}
currentPlayer = 0
lock = threading.Lock()

def handle_client():
    global currentPlayer
    while True:
        data, addr = s.recvfrom(2048)
        data = pickle.loads(data)

        if addr not in addresses:
            with lock:
            # used in multithreaded programs to prevent race conditions
            # where multiple threads access shared resources concurrently,
            # potentially leading to unpredictable behavior or data corruption
                addresses[addr] = currentPlayer
                currentPlayer += 1
            game_id = addresses[addr] // 2
            player_id = addresses[addr] % 2
            s.sendto(pickle.dumps(games[game_id][player_id]), addr)
            continue

        game_id = addresses[addr] // 2
        player_id = addresses[addr] % 2
        games[game_id][player_id] = data

        if player_id == 1:
            reply = games[game_id][0]
        else:
            reply = games[game_id][1]

        s.sendto(pickle.dumps(reply), addr)


thread = threading.Thread(target=handle_client)
thread.start()
