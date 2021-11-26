from socket import *
from threading import Thread  # threads usage
import sys  # In order to terminate the program


class ServerThread(Thread):  # Creating the thread class.

    def __init__(self, ip: int, port: int, socket):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print("[+] New Socket -> " + str(ip) + ":" + str(port))

    def run(self):
        while True:
            print('Ready to serve...')
            tcp_connection, addr = tcp_server_socket.accept()  # obtaining established connection from the backlog queue.
            try:
                message = tcp_connection.recv(1024).decode()  # decoding the message to bits.
                filename = message.split()[1]
                f = open(filename[1:])

                # sending a basic message to our client, including HTTP Header :
                output_data = []
                output_data.append("HTTP/1.1 200 OK\r\n")
                output_data.append("Content-Type: text/html; charset=utf-8\r\n\r\n")
                output_data.append("<html><body>Hello World</body></html>\r\n\r\n")

                for i in range(0,
                               len(output_data)):  # can use also send all instead, right now for this project using this.
                    tcp_connection.send(output_data[i].encode())  # encoding bits to real language.
                tcp_connection.send("\r\n".encode())  # encoding bits to real language.

                tcp_connection.close()
                break

            except IOError:
                # Send response message for file not found
                # the idea below is like the above, sending an error message if the name server is incorrect.
                error_data = []
                error_data.append('HTTP/1.1 404 Not Found\r\n')
                error_data.append('Content-Type: text/html\r\n\r\n')
                error_data.append('<html><head></head><body>404 Not Found</body></html>')
                for i in range(0,
                               len(error_data)):  # can use also send all instead, right now for this project using this.
                    tcp_connection.send(error_data[i].encode())  # encoding bits to real language.
                tcp_connection.send("\r\n".encode())  # encoding bits to real language.
                tcp_connection.close()
                break


if __name__ == '__main__':

    TCP_address = '127.0.0.1'
    TCP_port = 12000

    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind((TCP_address, TCP_port))

    print("Waiting for connections from TCP clients...")
    tcp_server_socket.listen(4)  # up to 4 clients can connect
    while True:
        tcp_connection, (ip, port) = tcp_server_socket.accept()
        new_thread = ServerThread(ip, port, tcp_server_socket)  # init a thread
        new_thread.run()  # run the thread.

