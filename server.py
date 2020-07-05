from clientServerModel import *
import random
from certificationAuthority import certificationAuthority
from myRSA import myRSA
from blumFairness import blumFairness
from datetime import time
from diffieHelman import diffieHelman
from datetime import date
import sys
class server(clientServerModel):
    
    def __init__(self, player, connection):
        super(server, self).__init__(player, connection)
    
    def noFairness(self):
        super(server, self).getConnection().setPort(10000)
        super(server, self).getConnection().serverCreateConnection()
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(24)), end="\n\n")#1
        res = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(27))#2
        super(server, self).getPlayer().setOpposite(res)
        print(super(server, self).getPlayer().getOtherOne() + ": ", res, end="\n\n")
        res = self.__flipCoinWNoFairness()
        super(server, self).getConnection().serverSendReceiveMessage(res)#3
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().haveIWon(res)) , end="\n\n")#EXTRA
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#4
        super(server, self).getConnection().closeConnection()
    
    def blumFairness(self):
        super(server, self).getConnection().setPort(10200)
        super(server, self).getConnection().serverCreateConnection()
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(47)), end="\n\n")#1
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(34)), end="\n\n")#2
        rawKey = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(36))#3
        rawKeySplitted = rawKey.split(" ")
        rawKeySplitted[0] = int(rawKeySplitted[0])
        rawKeySplitted[1] = int(rawKeySplitted[1])
        super(server, self).getPlayer().setMyDiffieHelmanKey(diffieHelman(rawKeySplitted[0], rawKeySplitted[1], random.randint(100,999)))
        dhKey = super(server, self).getPlayer().getMyDiffieHelmanKey()
        print(super(server, self).getPlayer().getOtherOne() + ": ", rawKey, end="\n\n")
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(29)), end="\n\n")#4
        partialKey = dhKey.generatePartialKey()
        partialKeyToString = str(partialKey)
        partialKeyFromOtherOne = super(server, self).getConnection().serverSendReceiveMessage(partialKeyToString)#5
        print(super(server, self).getPlayer().getOtherOne() + ": ", partialKeyFromOtherOne, end="\n\n")
        partialKeyFromOtherOneToInt = int(partialKeyFromOtherOne)
        dhKey.generateFullKey(partialKeyFromOtherOneToInt)
        encryptedMessage = super(server, self).getConnection().serverSendReceiveMessage(dhKey.encryptMessage(super(server, self).getPlayer().getStuffToSayElement(22)))#6
        print(super(server, self).getPlayer().getOtherOne() + ": ", encryptedMessage," -> ", dhKey.decryptMessage(encryptedMessage), end="\n\n")
        encryptedMessage = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(37))#7
        print(super(server, self).getPlayer().getOtherOne() + ": ", encryptedMessage," -> ", dhKey.decryptMessage(encryptedMessage))
        decryptedMessage = dhKey.decryptMessage(encryptedMessage)
        super(server, self).getPlayer().setMyBlum(blumFairness.createFromRaw(decryptedMessage, 200, 4, True))
        blum = super(server, self).getPlayer().getMyBlum()
        if(blum == 0):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(39)), end="\n\n")#8
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#9
            super(server, self).getConnection().closeConnection()
        elif(blum == 1):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(40)), end="\n\n")#8
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#9
            super(server, self).getConnection().closeConnection()
        elif(blum == 2):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(41)), end="\n\n")#8
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#9
            super(server, self).getConnection().closeConnection()
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(38)), end="\n\n")#8
        blum.randomBits(4)
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(blumFairness.format(blum.getBits())), end="\n\n")#9
        messageFromOtherOne = super(server, self).getConnection().serverSendReceiveMessage(" ")#10
        print(super(server, self).getPlayer().getOtherOne() + ": ", messageFromOtherOne,end = "\n\n")
        if(not blum.controlBits(messageFromOtherOne)):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(42)), end="\n\n")#11
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#12
            super(server, self).getConnection().closeConnection()
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(43)), end="\n\n")#11
        blum.setSquareX(11)
        myMessage = str(blum.getN()) + "," + str(date.today()) + "," + blumFairness.format(blum.getXSquaredValues()) + "," + super(server, self).getPlayer().getStuffToSayElement(44)
        super(server, self).getConnection().serverSendReceiveMessage(dhKey.encryptMessage(myMessage))#12
        encryptedMessageFromOtherOne = super(server, self).getConnection().serverSendReceiveMessage(" ")#13
        print(super(server, self).getPlayer().getOtherOne() + ": ", encryptedMessageFromOtherOne," -> ", dhKey.decryptMessage(encryptedMessageFromOtherOne), end="\n\n")
        decryptedMessageFromOtherOne = dhKey.decryptMessage(encryptedMessageFromOtherOne)
        resultValue = blum.syntaxControl(decryptedMessageFromOtherOne, 3, 11)
        if(resultValue == 0):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(40)), end="\n\n")#14
            super(server, self).getConnection().closeConnection()
        elif(resultValue == 1):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(45)), end="\n\n")#14
            super(server, self).getConnection().closeConnection()
        elif(resultValue == 2):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(41)), end="\n\n")#14
            super(server, self).getConnection().closeConnection()
        elif(resultValue == 3):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(41)), end="\n\n")#14
            super(server, self).getConnection().closeConnection()
        super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(46))#14
        super(server, self).getConnection().serverSendReceiveMessage(blumFairness.format(blum.getXValuesUsed()))#15
        finalResult = blum.checkResult(blum.getXValuesUsed(), super(server, self).getPlayer().getName())
        if(finalResult == "Won"):
            ans = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(31))#16
        elif(finalResult == "Lost"):
            ans = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(30))#16
        else:
            ans = super(server, self).getConnection().serverSendReceiveMessage(" ")#16
        print(super(server, self).getPlayer().getOtherOne() + ": ",ans, end="\n\n")
        if(len(ans) < 57):
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(26)), end="\n\n")#17
        else:
            print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(45)), end="\n\n")#17
        super(server, self).getConnection().closeConnection()
    
    def rsaFairness(self):
        super(server, self).getConnection().setPort(10300)
        super(server, self).getConnection().serverCreateConnection()
        super(server, self).getPlayer().setMyRSA(myRSA())
        rsa = super(server, self).getPlayer().getMyRSA()
        if(not certificationAuthority.loadCA(rsa.getPubKey().n, rsa.getPubKey().e, super(server, self).getPlayer().getName())):
            super(server, self).getConnection().closeConnection()

        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(24)), end="\n\n") #1

        toSign = super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(27)) #2
        print(super(server, self).getPlayer().getOtherOne() + ": ", toSign, end="\n\n")

        flip = self.__flipCoinWFairness()
        encryptedMessage = rsa.signature(flip)
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(encryptedMessage), end="\n\n") #3

        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(28)), end="\n\n") #4

        pubKeyOtherOneRAW = super(server, self).getConnection().serverSendReceiveMessage(rsa.getRawPubKey())
        keyOtherOne = rsa.setPubKeyFromRaw(pubKeyOtherOneRAW)
        print(super(server, self).getPlayer().getOtherOne() + ": ", keyOtherOne.getPubKey(), end="\n\n") #5

        if(not certificationAuthority.checkCA(pubKeyOtherOneRAW, super(server, self).getPlayer().getOtherOne())):
            super(server, self).getConnection().closeConnection()
        else:
            print("signature check della chiave pubblica di " + super(server, self).getPlayer().getOtherOne() + " via CA ha confermato l'identità del mittente  \n")

        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().serverSendReceiveMessage(super(server, self).getPlayer().getStuffToSayElement(29)), end="\n\n") #6

        myChoiceEncrypted = rsa.encrypt(flip, keyOtherOne.getPubKey())
        otherOneData = super(server, self).getConnection().serverSendReceiveMessage(myChoiceEncrypted)
        print(super(server, self).getPlayer().getOtherOne() + ": ", otherOneData, end="\n\n") #7

        finalResult = rsa.decrypt(otherOneData)
        finalResult = finalResult.decode('utf8')
        print(super(server, self).getPlayer().getOtherOne() + " ha scelto, ", finalResult, end="\n\n")
        print(super(server, self).getPlayer().getOtherOne() + ": ", super(server, self).getConnection().clientSendReceiveMessage(super(server, self).getPlayer().getRSAResult(finalResult, toSign, keyOtherOne.getPubKey())), end="\n\n")#8

        super(server, self).getConnection().closeConnection()
    
    def __flipCoinWNoFairness(self):
        maxDraw = 11
        i = 0
        check = 0
        ans = ""
        while(i < maxDraw):
            if(check < 5):
                resp = random.randrange(0,100)
                if(resp < 50):
                    res = "testa"
                else:
                    res = "croce"
                if(super(server, self).getPlayer().getChoice() != res):
                    check += 1
            else:
                res = super(server, self).getPlayer().getChoice()
            ans = ans + res + " "
            i += 1
        return ans
    
    def __flipCoinWFairness(self):
        maxDraw = 11
        i = 0
        ans = ""
        while(i < maxDraw):
            resp = random.randrange(0,100)
            if(resp < 50):
                res = "testa"
            else:
                res = "croce"
            i = i + 1
            ans = ans + res + " "
        return ans