#Echo client, copied from https://realpython.com/python-sockets/

import socket

HOST=input("Enter address of server: ")
PORT= 19278
message=input("Enter message: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(message.encode('UTF-8'))
    data=s.recv(1024)

print(f"Received {data!r}")
