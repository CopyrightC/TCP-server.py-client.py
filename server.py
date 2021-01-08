#!/usr/bin/env python3

import socket

HOST = '0.0.0.0' # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            msg = input("-> ")
            data = conn.recv(1024)
            data =data.decode()
            print(data)
            if not data:
                break
            conn.send(msg.encode())
    
