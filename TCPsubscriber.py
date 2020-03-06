import socket
import select
import time
import sys, os

def mainRun():
    data = input("Subscriber IP: ")
    splitData = data.split()
    if splitData[0] == 'q':
        print("Bye ..")
    else:
        host = splitData[1]
        port = 50000
        server = socket.socket()
        server.connect((host,port))
            # receive & send data
        server.send(data.encode('utf-8'))
        try:
            while True:
                ready = select.select([server], [], [], 0.1)
                if ready[0]:
                    data = server.recv(1024).decode('utf-8')
                    print("Data from publisher : " + data  )
                else:
                    time.sleep(0.1)
                    pass
        except KeyboardInterrupt:
            print ('Interrupted ..')
            try:
                message = 'q'
                server.send(message.encode('utf-8'))
                server.close()
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        
        
        server.close()
if __name__ == "__main__":
    mainRun() 