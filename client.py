import socket
import os,sys

def client():
  

  host = socket.gethostbyname('localhost')  # get local machine name
  port = 50000  # Make sure it's within the > 1024 $$ <65535 range
  print(host)
  s = socket.socket()
  s.connect((host, port))
  
  message = input('==> ')
  # while message != 'q':
  if message == 'q':
    s.send(message.encode('utf-8'))
    s.close
  else:
    s.send(message.encode('utf-8'))
    try:
      while(True):
        pass
    except KeyboardInterrupt:
      print ('Interrupted ..')
      try:
        print("message")
        message = 'q'
        s.send(message.encode('utf-8'))
        s.close()
        sys.exit(0)
      except SystemExit:
        os._exit(0)
    # data = s.recv(1024).decode('utf-8')
    # print('Received from server: ' + data)
    # message = input('==> ')

# subscriber 127.0.0.1 room1

if __name__ == '__main__':
    client()