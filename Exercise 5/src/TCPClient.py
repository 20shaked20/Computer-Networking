from socket import *

serverName = 'localhost'
serverPort = 12000
SERVER_ADDRESS = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(SERVER_ADDRESS)
while True:
    msg = input('send message: ')
    if msg == 'END':
        clientSocket.close()
        break
    clientSocket.send(msg.encode())
    modifiedSentence = clientSocket.recv(1024)
    if modifiedSentence.decode() == 'END':
        clientSocket.close()
    print('From Server:', modifiedSentence.decode())
