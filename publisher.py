import socket
import sys, os
import threading
import time

def close_connect(s):
    txtout = "q"
    s.send(txtout.encode('utf-8'))
    s.close()
    print("\nTime out : Close connect")
    os._exit(0)

def publish():
    SERV_PORT = 50000
    data = input("publisher> ")
    splitData = data.split()
    if splitData[0] == 'q':
        print("Bye ..")
    else:
        host = splitData[1]
        addr = (host, SERV_PORT)
        s = socket.socket()
        try:
            s.connect(addr)
        except ConnectionError:
            print("Connection Error")
            return
        s.send(data.encode('utf-8'))
        t = threading.Timer(1, close_connect, [s])
        try:
            while True:
                t.start()
                txtout = input("publisher> ")
                t.cancel()
                s.send(txtout.encode('utf-8'))
                if txtout == 'q':
                    print("Bye ..")
                    break
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
    publish()
