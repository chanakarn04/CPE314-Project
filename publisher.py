import socket
import sys, os

def publish():
    SERV_PORT = 50000
    data = input("publisher > ")
    splitData = data.split()
    host = splitData[1]
    addr = (host, SERV_PORT)
    s = socket.socket()
    try:
        s.connect(addr)
    except ConnectionError:
        print("Connection Error")
        return
    s.send(data.encode('utf-8'))
    try:
        while True:
            txtout = input("publisher > ")
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
