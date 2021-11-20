# Python TCP Client A
import socket

Server_name = 'localhost'
T_server_port = 12000
SERVER_ADDRESS = (Server_name, T_server_port)

BUFFER_SIZE = 2048  # recv

MESSAGE = input("ClientA: Enter message/ Enter exit: ")

ClientA_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientA_socket.connect(SERVER_ADDRESS)

while MESSAGE != 'exit':
    ClientA_socket.send(MESSAGE.encode())
    data = ClientA_socket.recv(BUFFER_SIZE)
    print("ClientA received data:", data)
    MESSAGE = input("ClientA: Enter message to continue/ Enter exit: ")

ClientA_socket.close()
