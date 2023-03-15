
import socket
import lib.VisualEffect as ve
import importlib
import sys,os
from datetime import datetime


def current_time():
    now = datetime.now()

    ct = now.strftime("%H:%M:%S")

    ct = ve.blue("["+ct+"] ")
    return ct


def startServer(host = "127.0.0.1",port = 8050,max_conn = 5):



    print(current_time()+ve.green("Server Started on "+host+":"+str(port)))

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(max_conn)

    while(True):
        conn, address = server_socket.accept()
        print(current_time()+ve.yellow("Connection from: " + str(address)))


        data = conn.recv(1024).decode()
        response = ve.orange("<?>")


        if data:
            if(str(data).strip().lower() == "shutdown"):
                print(current_time()+ve.orange("Server is Shutting Down!"))
                conn.send(ve.orange("Server is Shutting Down").encode())
                conn.close()
                break              

            elif(str(data).strip().lower() == "echo"):
                print(current_time()+"Sending Echo!")
                response = ve.yellow(" > ")+"Server Echo"

            elif(str(data).strip().lower() == "services"):
                print(current_time()+"Sending Service List...")
                print(ve.cyan("<START: ServiceList>\n"))
                list = os.listdir("services/")
                response = ve.cyan("Services:\n")
                for serv in list:
                    if(".py" in serv):
                        print(serv.replace(".py",""))
                        response+=ve.yellow(" > ")+serv.replace(".py","")+"\n"
                print(ve.cyan("\n<END: ServiceList>"))

            elif(str(data).strip().lower() == "?"):
                print(current_time()+"Sending Command List...")
                print(ve.cyan("<START: CommandList>\n"))
                response = ve.cyan("Commands:\n")
                print("shutdown\necho\nservices\n?\n{service_name}")
                response += ve.yellow(" > ")+"shutdown\n"+ve.yellow(" > ")+"echo\n"+ve.yellow(" > ")+"services\n"+ve.yellow(" > ")+"?\n"+ve.yellow(" > ")+"{service_name}"
                print(ve.cyan("\n<END: CommandList>"))

            elif(str(data).strip().lower() == ""):
                print(current_time()+ve.red("<?>"))

            else:

                mod = "services."+str(data).lower().strip()
                out = ""
                try:
                    print(current_time()+"Sending Service...")
                    imp = importlib.import_module(mod, package=None)
                    out = imp.run()
                    print(ve.cyan("<START: ServiceOutput>\n"))
                    print(out)
                    print(ve.cyan("\n<END: ServiceOutput>"))
                except ModuleNotFoundError as err:
                    print(current_time()+ve.red("Error: Module Not Found Error"))
                    out = ve.red("Error: Module Not Found Error")

                response = out

            conn.send(response.encode())

        conn.close()
    server_socket.close()



if(len(sys.argv)==2):
    if(sys.argv[1] == "?"):
        print("Args: [Host][Port][Max_Connections]")
    else:
        startServer(sys.argv[1])
elif(len(sys.argv)==3):
    startServer(sys.argv[1],int(sys.argv[2]))
elif(len(sys.argv)==4):
    startServer(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
else:
    startServer()

