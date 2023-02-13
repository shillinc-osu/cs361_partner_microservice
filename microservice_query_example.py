import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65434  # The port used by the server

print('Sending the stock symbol for Meta.')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"META")
    data = s.recv(65536)

f = open("metaStock.csv", "w")
f.write(data.decode())
f.close()