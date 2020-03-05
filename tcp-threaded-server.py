import socket
from threading import Thread
import os,sys

def handle_client(s):
  while True:
    txtin = s.recv(1024)
    print ('Client> %s' %(txtin).decode('utf-8')) 
    if not txtin:
      print('Client disconnected ...')
      break
    else:
      txtout = txtin.upper()    
      s.send(txtout)
  s.close()
  return

def main():
    host = socket.gethostname()
    port = 50000
    addr = (host, port)
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print ('TCP threaded server started ...')

    while True:
      sckt, addr = s.accept()
      ip, port = str(addr[0]), str(addr[1]) 
      print ('New client connected from ..' + ip + ':' + port)
      try:
        Thread(target=handle_client, args=(sckt,)).start()
      except:
        print("Cannot start thread..")
        import traceback
        trackback.print_exc()

    s.close()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print ('Interrupted ..')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
