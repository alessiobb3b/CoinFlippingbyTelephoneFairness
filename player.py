from diffieHelman import diffieHelman
import random
from names import names
class player:

    def setMyDiffieHelmanKey(self, key):
        self.myDiffieHelmanKey = key
    
    def getMyDiffieHelmanKey(self):
        return self.myDiffieHelmanKey
    
    def setMyRSA(self, key):
        self.myRSA = key
    
    def getMyRSA(self):
        return self.myRSA
    
    def setMyBlum(self, key):
        self.myBlum = key
    
    def getMyBlum(self):
        return self.myBlum
    
    def setOtherOne(self, name):
        self.otherOne = name
    
    def editStuffToSay(self):
        temp = []
        for elem in self.getStuffToSay():
            elem = elem.replace("MYNAME", self.getName())
            elem = elem.replace("OTHERONE", self.getOtherOne())
            temp.append(elem.rstrip())
        self.setStuffToSayNewOne(temp)

    def setStuffToSay(self):
        file = open('stuffToSay.txt', 'r') 
        self.stuffToSay = file.readlines() 
    
    def setStuffToSayNewOne(self, value):
        self.stuffToSay = value
    
    def setName(self, name):
        self.name = name
        self.setOtherOne(names().getServerName()) if self.client() else self.setOtherOne(names().getClientName())
    
    def setIsClient(self, isClient):
        self.isClient = isClient
    
    def getName(self):
        return self.name
    
    def setChoice(self, choice):
        self.choice = choice
    
    def getChoice(self):
        return self.choice
    
    def getStuffToSayElement(self, i):
        return self.stuffToSay[i]
    
    def getStuffToSay(self):
        return self.stuffToSay
    
    def getOtherOne(self):
        return self.otherOne
    
    def client(self):
        return self.isClient
    
    def setOpposite(self, value):
        value = value.lower()
        self.setChoice("testa") if value == "croce" else self.setChoice("croce")

    def haveIWon(self, values):
        flipped = values.split(' ')
        flipped.pop()
        points = 0
        for elem in flipped:
            if(elem.lower() == self.getChoice()):
                points += 1
        if(points > 5):
            return self.getStuffToSayElement(8) if self.client() else self.getStuffToSayElement(31)
        else:
            return self.getStuffToSayElement(1) if self.client() else self.getStuffToSayElement(30)
    
    def getRSAResult(self, finalResult, signature, pubKeyOtherOne):
        rsa = self.getMyRSA()
        temp = self.getStuffToSayElement(25) + " "
        if(rsa.verifySignature(finalResult, signature, pubKeyOtherOne) == 'SHA-1'):
            temp += self.haveIWon(finalResult) + " " + self.getStuffToSayElement(26)
        else:
            temp += self.getStuffToSayElement(5)
        return temp
    
    def generateDiffieHelmanKey(self):
        primes = open("PrimeNumbers.txt",'r')
        primes = primes.read()
        primes = primes.split(', ')
        q = random.randint(0,len(primes)-1)
        p = int(primes[q])
        q = q + 1
        b = random.randint(100,999)
        self.setMyDiffieHelmanKey(diffieHelman(p,q,b))

    def __init__(self, name, choice, isClient):
        self.setChoice(choice)
        self.setStuffToSay()
        self.setIsClient(isClient)
        self.setName(name)
        self.editStuffToSay()