# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP connection

serverPort = 12000  # server port, basic one
SERVER_ADDRESS = ('', serverPort)  # creating server address

serverSocket.bind(SERVER_ADDRESS)  # binding the server
serverSocket.listen(1)  # listen to 1 client

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # obtaining established connection from the backlog queue.
    try:
        message = connectionSocket.recv(2048).decode()  # decoding the message to bits.
        filename = message.split()[1]
        f = open(filename[1:])

        # sending a basic message to our client, including HTTP Header :
        output_data = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(output_data)):  # can use also send all instead, right now for this project using this.
            connectionSocket.send(output_data[i].encode())  # encoding bits to real language.
        connectionSocket.send("\r\n".encode())  # encoding bits to real language.
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # the idea below is like the above, sending an error message if the name server is incorrect.
        error_data = []
        error_data.append('HTTP/1.1 404 Not Found\r\n')
        error_data.append('Content-Type: text/html\r\n\r\n')
        error_data.append('<html><head></head><body>404 File Not Found</body></html>')
        for i in range(0, len(error_data)):  # can use also send all instead, right now for this project using this.
            connectionSocket.send(error_data[i].encode())  # encoding bits to real language.
        connectionSocket.send("\r\n".encode())  # encoding bits to real language.

        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
