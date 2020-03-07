import socket
import sys

def publish():
    MAX_BUF = 1024
    SERV_PORT = 50000
    data = input("publisher IP: ")
    splitData = data.split()
    if splitData[0] == 'q':
        print("Bye ..")
    else:
        host = splitData[1]
        addr = (host, SERV_PORT)
        s = socket.socket()
        s.connect(addr)
        s.send(data.encode('utf-8'))
        while True:
            txtout = input("Publisher>>")
            s.send(txtout.encode('utf-8'))
            if txtout == 'q':
                print("Bye ..")
                break
        # while True:
        #     txtout = input("Publisher>> ")
        #     s.send(txtout.encode('utf-8'))
        #     if txtout == 'q':
        #         print("Bye")
        #         break
        s.close()


# publisher 127.0.0.1 room1 HelloWorld

# subscriber 127.0.0.1 room1

if __name__ == "__main__":
    publish()
