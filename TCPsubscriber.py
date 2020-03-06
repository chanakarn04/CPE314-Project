import socket

def mainRun():
    data = input("Subscriber IP:")
    splitData = data.split()
    host = splitData[1]
    port = 50000
    server = socket.socket()
    server.connect((host,port))
        #receive & send data
    server.send(data.encode('utf-8'))
    while data!='q':
        data = server.recv(1024).decode('utf-8')
        print("Data from publisher : " + data  )
        # data = input("input message :")
    server.close()
if __name__ == "__main__":
    mainRun() 