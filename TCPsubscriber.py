import socket

def mainRun():
    host = "127.0.0.1"
    port = 5000
    server = socket.socket()
    server.connect((host,port))
    data = input("input message :")

        #receive & send data
    while data!='q':
        server.send(data.encode('utf-8'))
        data = server.recv(1024).decode('utf-8')
        print("Data from Server : " + data)
        data = input("input message :")
    server.close()
if __name__ == "__main__":
    mainRun() 