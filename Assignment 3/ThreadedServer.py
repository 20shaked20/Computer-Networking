import socket
from threading import Thread


# TCP Server Socket Thread Pool
class ServerThread(Thread):

    def __init__(self, ip: int, port: int):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("Added New server socket thread started for " + str(ip) + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            print("Server received data: ", data)
            MESSAGE = input("Enter Response from Server/Enter exit: ")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode())  # echo


# TCP Server Socket Program Stub
TCP_address = '127.0.0.1'
TCP_port = 12000
BUFFER_SIZE = 20  # Usually 1024, but we need quick response (recv)

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server.bind((TCP_address, TCP_port))
threads = []

while True:
    tcp_server.listen(4)  # up to four clients.
    print("Waiting for connections from TCP clients...")
    (conn, (ip, port)) = tcp_server.accept()
    new_thread = ServerThread(ip, port)  # init a thread.
    new_thread.start()
    threads.append(new_thread)  # added to the list.

for t in threads:
    t.join()
