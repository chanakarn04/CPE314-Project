import socket
import sys

def publish():
    MAX_BUF = 1024
    SERV_PORT = 50000
    data = input("publisher IP: ")
    splitData = data.split()
    host = splitData[1]
    addr = (host, SERV_PORT)
    s = socket.socket()
    s.connect(addr)
    s.send(data.encode('utf-8'))
    while True:
        txtout = input("Publisher>> ")
        s.send(txtout.encode('utf-8'))
        if txtout == 'quit':
            break


publish()
