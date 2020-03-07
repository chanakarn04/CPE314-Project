import socket
import select
import time
import sys, os

def subscribe():
    data = input("Subscriber IP: ")
    splitData = data.split()
    if splitData[0] == 'q':
        print("Bye ..")
    else:
        host = splitData[1]
        port = 50000
        s = socket.socket()
        s.connect((host,port))
            # receive & send data
        s.send(data.encode('utf-8'))
        try:
            while True:
                ready = select.select([s], [], [], 0.1)
                if ready[0]:
                    data = s.recv(1024).decode('utf-8')
                    print("Data from publisher : " + data  )
                else:
                    time.sleep(0.1)
                    pass
        except KeyboardInterrupt:
            print ('Interrupted ..')
            try:
                message = 'q'
                s.send(message.encode('utf-8'))
                s.close()
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        s.close()

if __name__ == "__main__":
    subscribe()