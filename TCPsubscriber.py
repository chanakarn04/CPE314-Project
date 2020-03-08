import socket
import select
import time
import sys, os

TIME_OUT = 60

def subscribe():
    data = input("subscriber> ")
    splitData = data.split()
    startTime = time.time()
    if splitData[0] == 'q':
        print("Bye ..")
    else:
        host = splitData[1]
        port = 50000
        s = socket.socket()
        try:
            s.connect((host,port))
        except ConnectionError:
            print("Connection Error")
            return
        s.send(data.encode('utf-8'))
        try:
            while True:
                if time.time() - startTime > TIME_OUT:
                    try:
                        message = 'q'
                        s.send(message.encode('utf-8'))
                        s.close()
                        sys.exit(0)
                    except SystemExit:
                        os._exit(0)
                    break
                ready = select.select([s], [], [], 0.1)
                if ready[0]:
                    data = s.recv(1024).decode('utf-8')
                    startTime = time.time()
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

if __name__ == "__main__":
    subscribe()