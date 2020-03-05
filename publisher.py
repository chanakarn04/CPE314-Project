import socket
import sys

def publish():
    MAX_BUF = 2048
    SERV_PORT = 50000

    addr = ('127.0.0.1', SERV_PORT)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(addr)
    while True:
        print('Publisher>> ', end='')
        sys.stdout.flush()
        txtout = sys.stdin.readline().strip()
        s.send(txtout.encode('utf-8'))
        if txtout == 'quit':
            break
        ack = s.recv(MAX_BUF)
        print('\t' + ack.decode('utf-8'))