# Python TCP Client B
import socket

Server_name = 'localhost'
T_server_port = 12000
SERVER_ADDRESS = (Server_name, T_server_port)

BUFFER_SIZE = 2048  # recv

MESSAGE = input("ClientB: Enter message/ Enter exit: ")

ClientB_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientB_socket.connect(SERVER_ADDRESS)

while MESSAGE != 'exit':
    ClientB_socket.send(MESSAGE.encode())
    data = ClientB_socket.recv(BUFFER_SIZE)
    print("ClientB received data:", data)
    MESSAGE = input("ClientB: Enter message to continue/ Enter exit: ")

ClientB_socket.close()
