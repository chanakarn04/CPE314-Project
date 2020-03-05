topicMsg = {'ip1':[], 'ip2':[], 'ip3':[], 'ip4':[]}
topicList = {'topic1': ['ip1','ip2','ip3','ip4']}

def send_message(client_socket, address):
  # send message back to subscriber
  while True:
    data = topicMsg[address(0)].pop(0)
    client_socket.send(data.encode('utf-8'))
  client_socket.close()

def publisher_service(topic, message):
  try:
    sub_ip = topicList[topic]
  except KeyError:
      print("Topic does not exist")
  else:
     for sb in sub_ip:
      topicMsg[sb].append([topic, message])
      print(topicMsg)
  
# publisher_service('topic1', 'this is message')
# publisher_service('topic2', 'this is message')
# publisher_service('topic3', 'this is message')