#Echo server, copied from https://realpython.com/python-sockets/

import socket

HOST = "" #Empty string to bind to all interfaces
PORT = 19278

#Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()#gives a default backlog value
    conn,addr = s.accept() #blocks, waiting for incoming connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) #Get 1024 bytes at a time from the socket.
            if not data:
                break
            conn.sendall(data) #echo back the same message
