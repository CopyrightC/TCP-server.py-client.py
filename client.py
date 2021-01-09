import socket
import os
import sys
HOST = ''#ipv4 of host  
PORT = #port here
idx = socket.gethostname()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(idx.encode())
    ifban = s.recv(1024)
    ifban = ifban.decode()
    if ifban.startswith("You are not"):
        print(ifban)
        sys.exit()
    usrn = input("Enter your username : ")
    s.send(f"{usrn} wants to join the chat, would you like to allow (y/n)?".encode())
    while True:
        permissionx = s.recv(1024)
        permissionx = permissionx.decode()
        if permissionx == "y":
            print("Server has allowed your entry!")
            break
        else:
            print("Server has declined your request to join the chat room")
            quit()
    s.send(f"{usrn} has connected to chat!".encode())
    while True:
        x = input("YOU : ")
        x = f"{usrn} : {x}"
        try:
            s.send(x.encode())
            data = s.recv(1024)
            data = data.decode()
            if data == "You have been banned by the server!":
                print(data)
                sys.exit()
            if data == f"{usrn}.kick":
                print('You were kicked by the server')
                sys.exit()
            else: print(data)
        except ConnectionResetError:
            print("Server is offline")
            quit()
