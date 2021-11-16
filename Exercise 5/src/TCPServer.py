from socket import *

serverPort = 12000
SERVER_ADDRESS = ('', serverPort)
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(SERVER_ADDRESS)
serverSocket.listen(1)
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()
while True:

    sentence = connectionSocket.recv(1024).decode()
    print(f"the client: {sentence}")
    msg = input('my message: ')
    if sentence == 'END':
        connectionSocket.close()
        break
    connectionSocket.send(bytes(msg.encode()))
    if msg == 'END':
        connectionSocket.close()
        break
