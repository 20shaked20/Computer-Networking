from socket import *

serverPort = 12000
SERVER_ADDRESS = ('', serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(SERVER_ADDRESS)
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
