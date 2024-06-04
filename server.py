import socket

serverIp = '127.0.0.1'
port = 9999

server = socket.socket()

server.bind((serverIp, port))
server.listen(1)

client, adder = server.accept()

msg = client.recv(1024)

print(msg)

client.send(b"hi")

client.close()