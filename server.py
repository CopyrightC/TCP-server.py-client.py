import socket
import io
import sys
HOST = #hostip
PORT = #>1024
bans = []
try:
    with open("bans.txt","r") as xban1:
        all_bans = xban1.read()
        xban1.close()
        bans.append(all_bans)
except io.UnsupportedOperation:
    pass
print(bans)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    idx = conn.recv(1024)
    client_id = idx.decode()
    if str(client_id) in bans:
        conn.send("You are not allowed to join that chat room (Reason : Banned by the server)".encode())
        print(f"Banned user {client_id} tried to join")
    else:
        conn.send("Legit".encode())
    with conn:
        usr = input("Enter your username : ")
        x = conn.recv(1024)
        x = x.decode()
        print(x)
        permisssion = input("y/n : ")
        conn.send(permisssion.encode())
        while True:
            try:
                confirm_joining = conn.recv(1024)
                confirm_joining=confirm_joining.decode()
                print(confirm_joining)
                break
            except:
                pass
        while True:
            msg = input("YOU : ")
            if msg.endswith('.ban'):
                bans.append(addr)
                msg = msg.split('.')
                print(f"{msg[0]} was banned!" )
                conn.send("You have been banned by the server!".encode())
                with open("bans.txt","w") as xban:
                    xban.write(str(client_id))
                    xban.close()
                    sys.exit()
            elif msg.endswith('.kick'):
                conn.send(msg.encode())
                msg = msg.split(".")
                print(msg[0],"was kicked!")
                sys.exit()
            try:
                data = conn.recv(1024)
                data =data.decode()
                print(data)
            except ConnectionResetError:
                print("Client is currently offline!")
                quit()
            if not data:
                break
            msg = f"{usr} : {msg}"
            try:
                conn.send(msg.encode())
            except ConnectionResetError:
                pass   
