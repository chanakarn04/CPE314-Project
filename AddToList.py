# Importing defaultdict 
from collections import defaultdict 

def splitfunction(text):
    x = text.split()

    return x


def addtodict(topic,ip):
    #Create an empty dict
    mydict = {} 

    if topic in mydict.keys():
        print("in if")
        mydict[topic].append(ip)
    else:
        print("in else")
        mydict[topic] = ip

    
    return mydict

    
#TestSplitFunction
x1 = splitfunction("222.222.555 thisistopic")
print("#TestSplitFunction")
print(x1)


#TestMydictFunction
topic = "TestTopic"
ip = '255.255.255'
print("#TestMydictFunction1")
mydict = addtodict(topic,ip)
print(mydict)

print("#TestMydictFunction2")
mydict = addtodict(topic,'555')
mydict = addtodict("topic2",'999')
print(mydict)


