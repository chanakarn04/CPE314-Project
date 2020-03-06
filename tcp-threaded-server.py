import socket
from threading import Thread
import os,sys

topicMsg = {}
# topicDict = {}

def splitfunction(text):
  x = text.split()
  return x

def createQueue(topic):
  if topic not in topicMsg.keys():
    topicMsg[topic] = []
  

# def addToDict(topic,ip):
#   print("add to dict")
#   if topic in topicDict.keys():
#       topicDict[topic].append(ip)
#       print(topicDict)
#   else:
#       lst = [ip]
#       topicDict[topic] = lst
#       print(topicDict)

# def send_message(client_socket, address):
#   while True:
#     data = topicMsg[address(0)].pop(0)
#     client_socket.send(data.encode('utf-8'))
#   client_socket.close()

def handle_publisher(s, ip, topic, message):
  check = False
  print("This is publisher")
  while True:
    if check:
      txtin = s.recv(1024)
      print ('Publisher> %s' %(txtin).decode('utf-8'))
      splitTxt = splitfunction(txtin.decode('utf-8')) 
    try:
      x = topicMsg[topic]
    except KeyError:
        print("Topic does not exist")
    else:
      topicMsg[topic].append(message)
      print(topicMsg)
      check = True

def handle_subscriber(s, topic, ip):
  # addToDict(topic, ip)
  createQueue(topic)
  print(topicMsg)
  print("This is subscriber")
  while True:
    if topicMsg[topic] != []:
      data = topicMsg[topic].pop()
      s.send(data.encode('utf-8'))
  s.close()

def handle_incoming_msg(sckt, address):
  createQueue(address[0])
  isHandle = False
  while(not isHandle):
    txtin = sckt.recv(1024)
    splitTxt = splitfunction(txtin.decode('utf-8'))
    if splitTxt[0] == "subscriber" :
      isHandle = True
      handle_subscriber(sckt, splitTxt[2], address[0])
    elif splitTxt[0] == "publisher" :
      isHandle = True      
      handle_publisher(sckt, address[0], splitTxt[2], splitTxt[3])
    else:
      print("Syntax error")

def main():
  # host = socket.gethostname()
  host = socket.gethostbyname('localhost')
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
      Thread(target=handle_incoming_msg, args=(sckt,addr,)).start()
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
