import socket

# hostname = socket.gethostname()    
# IPAddr = socket.gethostbyname(hostname)    
# print("Your Computer Name is: " + hostname)    
# print("Your Computer IP Address is: " + IPAddr) 

def server():
  host = socket.gethostname()   # get local machine name
  port = 50000  # Make sure it's within the > 1024 $$ <65535 range
  print("Server Start")
  s = socket.socket()
  s.bind((host, port))
  
#   s.listen(1)
#   client_socket, address = s.accept()
#   print(address[0])
#   print("Connection from: " + str(address))
#   while True:
#     data = client_socket.recv(1024).decode('utf-8')
#     if not data:
#       break
#     print('From online user: ' + data)
#     data = data.upper()
#     client_socket.send(data.encode('utf-8'))
#   client_socket.close()



topicMsg = {'ip1':[], 'ip2':[], 'ip3':[], 'ip4':[]}
topicList = {'topic1': ['ip1','ip2','ip3','ip4']}

def send_message(client_socket, address):
  while True:
    data = topicMsg[address(0)].pop(0)      # nutcxzx
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
      print("close connect")
      break
    print('From online user: ' + data)
    data = data.upper()
    client_socket.send(data.encode('utf-8'))
  client_socket.close()

# def publisher_service(topic, message):
#   try:
#     sub_ip = topicList[topic]
#   except KeyError:
#       print("Topic does not exist")
#   else:
#      for sb in sub_ip:
#       topicMsg[sb].append(message)
#       print(topicMsg)
  
# publisher_service('topic1', 'this is message')
# publisher_service('topic2', 'this is message')
# publisher_service('topic3', 'this is message')

if __name__ == '__main__':
    server()
