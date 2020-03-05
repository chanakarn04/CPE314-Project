mydict = {} 
def splitfunction(text):
    x = text.split()
    return x


def addtodict(topic,ip):
    if topic in mydict.keys():
        mydict[topic].append(ip)
    else:
        lst = [ip]
        mydict[topic] = lst

#TestSplitFunction
x1 = splitfunction("222.222.555 thisistopic")
print("#TestSplitFunction")
print(x1)

#TestMydictFunction
topic = "TestTopic"
ip = '255.255.255'
print("#TestMydictFunction1")
addtodict(topic,ip)
print(mydict)
print("#TestMydictFunction2")
addtodict(topic,'555')
addtodict("topic2",'999')
print(mydict)


