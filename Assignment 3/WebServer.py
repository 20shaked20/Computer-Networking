# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection

serverPort = 12000  # server port, basic one
SERVER_ADDRESS = ('127.0.0.1', serverPort)  # creating server address

serverSocket.bind(SERVER_ADDRESS)  # binding the server
serverSocket.listen(10)  # listen to 10 clients connection.

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # obtaining established connection from the backlog queue.
    try:
        message = connectionSocket.recv(5000).decode()  # decoding the message to bits.
        filename = message.split()[1]
        f = open(filename[1:])

        # sending a basic message to our client, including HTTP Header :
        outputdata = []
        outputdata.append("HTTP/1.1 200 OK\r\n")
        outputdata.append("Content-Type: text/html; charset=utf-8\r\n")
        outputdata.append("\r\n")
        outputdata.append("<html><body>Hello World</body></html>\r\n\r\n")

        for i in range(0, len(outputdata)):  # can use also send all instead, right now for this project using this.
            connectionSocket.send(outputdata[i].encode())  # encoding bits to real language.
        connectionSocket.send("\r\n".encode())  # encoding bits to real language.

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        print("\n 404 Not Found")
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
