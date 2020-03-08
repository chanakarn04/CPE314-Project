import socket
from threading import Thread, activeCount
import os,sys
import select

import time

topicMsg = {}
topicDict = {}

def splitfunction(text):
  x = text.split()
  return x

def handle_disconnect(sckt):
    ready = select.select([sckt], [], [], 0.25)
    if ready[0]:
        txtin = sckt.recv(1024)
        txt = txtin.decode('utf-8')
    else:
        txt = 'a'
    
    if txt == 'q':
        time.sleep(5)
        return True
    else:
        time.sleep(0.5)
        return False



def createQueue(ip, port):
  ipAndPort = str(ip) +":"+ str(port)
  if ipAndPort not in topicMsg.keys():
    topicMsg[ipAndPort] = []
  

def addToDict(topic, ipAndPort):
  if topic in topicDict.keys():
      topicDict[topic].append(ipAndPort)
  else:
      lst = [ipAndPort]
      topicDict[topic] = lst

def checkKey(dict, key): 
      
    if key in dict.keys(): 
        return True
    else: 
        return False

# def rmTopicDict(topic, ipAndPort):


def handle_publisher(s, ip, topic, message, port):
  check = False
  cond = False
  
  ipAndPort = str(ip) + ":" + str(port)
  while True:
    if check:
      txtin = s.recv(1024)
      splitTxt = splitfunction(txtin.decode('utf-8'))
      if splitTxt[0] == 'q':
        break
      elif len(splitTxt) == 4:
        print(" ==> Publisher has pulish in topic : " + str(splitTxt[2]) + ".\n ==>\tmessage : " + splitTxt[3])
        topic = splitTxt[2]
        message = splitTxt[3]
      else:
        print("syntax errer")
    try:
      subscriberList = topicDict[topic]
    except KeyError:
        print("Topic does not exist")
        check = True
    else:
      for queueTarget in subscriberList:
        topicMsg[queueTarget].append(message)
        check = True
      

  print('Publisher disconected ...')
  s.close()

def handle_subscriber(s, topic, ip, port):
  ipAndPort = str(ip) + ":" + str(port)
  addToDict(topic, ipAndPort)
  createQueue(ip, port)
  cond = False
  while not cond :
    cond = handle_disconnect(s)
    if topicMsg[ipAndPort] != []:
      data = topicMsg[ipAndPort].pop(0)
      s.send(data.encode('utf-8'))
    
  print('Subscriber disconected ...')
  s.close()

def handle_incoming_msg(sckt, address):
  isHandle = False
  print("Number of active child thread(s): " + str(activeCount() - 1))
  while(not isHandle):
    txtin = sckt.recv(1024)
    splitTxt = splitfunction(txtin.decode('utf-8'))
    if splitTxt[0] == 'q':
      print('Client disconected ...')
      sckt.close()
      print("Number of active child thread(s): " + str(activeCount() - 2))
      break
    elif splitTxt[0] == "subscriber" and len(splitTxt) == 3:
      isHandle = True
      print(" ==> New subscriber has subscribe in topic : " + str(splitTxt[2]))
      handle_subscriber(sckt, splitTxt[2], address[0], address[1])
    elif splitTxt[0] == "publisher" and len(splitTxt) == 4:
      isHandle = True
      print(" ==> Publisher has pulish in topic : " + str(splitTxt[2]) + ".\n ==>\tmessage : " + splitTxt[3])
      handle_publisher(sckt, address[0], splitTxt[2], splitTxt[3], address[1])
    else:
      print("Syntax error")

def main():
  host = socket.gethostbyname('localhost')
  port = 50000
  addr = (host, port)
  s = socket.socket()
  s.bind(addr)
  s.listen(1)
  print('TCP threaded server started ...')
  while True:
    sckt, addr = s.accept()
    print("New client connected from ... " + str(addr[0]) + ":" + str(addr[1]))
    try:
      Thread(target=handle_incoming_msg, args=(sckt,addr,)).start()
    except:
      print("Cannot start thread..")
      import traceback
      trackback.print_exc()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted ..')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
