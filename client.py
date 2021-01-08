#!/usr/bin/env python3
import socket
HOST = ''#host ipv4  
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        x = input("-> ")
        s.send(x.encode())
        data = s.recv(1024)
        data = data.decode()
        print(repr(data)