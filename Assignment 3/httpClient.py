import socket

Header = 64
Port = 12000
MSG = "Disconnected"
Server = "127.0.0.1"
ADDR = (Server, Port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode()
    msg_length = len(message)
    send_length = str(msg_length).encode()
    send_length += b'' * (Header - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode())


send("Shaked")
input()
send("")
input()
send(msg=MSG)
