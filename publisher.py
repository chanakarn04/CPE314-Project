import socket
import sys, os

def publish():
    SERV_PORT = 50000
    data = input("Server IP: ")
    splitData = data.split()
    host = splitData[0]
    addr = (host, SERV_PORT)
    s = socket.socket()
    s.connect(addr)
    try:
        while True:
            txtout = input("Publisher>> ")
            s.send(txtout.encode('utf-8'))
            if txtout == 'q':
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
