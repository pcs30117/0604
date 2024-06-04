import socket

serverIp = '127.0.0.1'
port = 9999

client = socket.socket()

client.connect((serverIp, port))

msg = input()

client.send(bytes(msg, 'euc-kr'))

msg = client.recv(1024)
print(msg)

client.close()