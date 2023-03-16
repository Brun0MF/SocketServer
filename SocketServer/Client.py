import socket
import sys


def sendCommandToServer(cmd = " ",host="127.0.0.1",port=8050):

    client_socket = socket.socket()
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    data = client_socket.recv(1024).decode()
    print(data)
    client_socket.close()


try:
    if(len(sys.argv)==2):
        if(sys.argv[1] == "?"):
            print("Args: [Command][Host][Port]")
        else:
            sendCommandToServer(sys.argv[1])
    elif(len(sys.argv)==3):
        sendCommandToServer(sys.argv[1],sys.argv[2])
    elif(len(sys.argv)==4):
        sendCommandToServer(sys.argv[1],sys.argv[2],int(sys.argv[3]))
    else:
        sendCommandToServer()
except Exception as ex:
    print("\033[91mError: "+str(ex)+"\033[00m")
