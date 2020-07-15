from clientServerModel import clientServerModel
from errorMessage import errorMessage
import time
from myRSA import myRSA
from certificationAuthority import certificationAuthority
from blumFairness import blumFairness
from datetime import date
import sys
class client(clientServerModel):
    
    def __init__(self, player, connection):
        super(client, self).__init__(player, connection)
    
    def noFairness(self):
        super(client, self).getConnection().setPort(10000)
        super(client, self).getConnection().createClientConnection()
        print(super(client, self).getPlayer().getName() + ": ",super(client, self).getPlayer().getStuffToSayElement(0),end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ",self.getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(0)), end="\n\n")#1
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ",super(client, self).getPlayer().getChoice(), end="\n\n\n")
        time.sleep(1) 
        print(super(client, self).getPlayer().getOtherOne() + ": ",self.getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getChoice()), end="\n\n")#2
        time.sleep(2)
        res = super(client, self).getConnection().clientSendReceiveMessage("...")#3
        print(super(client, self).getPlayer().getOtherOne() + ": ",res, end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getName() + ": ",super(client, self).getPlayer().haveIWon(res), end="\n\n")
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().haveIWon(res)), end="\n\n")#EXTRA
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(2)), end="\n\n")#4
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(2), end="\n\n")
        time.sleep(2)
        super(client, self).getConnection().closeConnection()
    
    def blumFairness(self):
        super(client, self).getConnection().setPort(10200)
        super(client, self).getConnection().createClientConnection()
        super(client, self).getPlayer().generateDiffieHelmanKey()
        dhKey = super(client, self).getPlayer().getMyDiffieHelmanKey()
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(0),end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(0)), end="\n\n")#1
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": " , super(client, self).getPlayer().getStuffToSayElement(9),end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(9)), end="\n\n")#2
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", dhKey.getPQRaw(),end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(dhKey.getPQRaw()), end="\n\n")#3
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(10),end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(10)), end="\n\n")#4
        partialkey = dhKey.generatePartialKey()
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", str(partialkey), end="\n\n")
        otherOnePartialKey = super(client, self).getConnection().clientSendReceiveMessage(str(partialkey))#5
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", otherOnePartialKey,end="\n\n")
        otherOnePartialKey = int(otherOnePartialKey)
        dhKey.generateFullKey(otherOnePartialKey)
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(22)," -> ", dhKey.encryptMessage(super(client, self).getPlayer().getStuffToSayElement(22)), end = "\n\n")
        encryptedMessageFromOtherOne = super(client, self).getConnection().clientSendReceiveMessage(dhKey.encryptMessage(super(client, self).getPlayer().getStuffToSayElement(22)))#6
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", encryptedMessageFromOtherOne," -> ", dhKey.decryptMessage(encryptedMessageFromOtherOne), end = "\n\n")
        time.sleep(1)
        super(client, self).getPlayer().setMyBlum(blumFairness(3, 200, 4))
        blum = super(client, self).getPlayer().getMyBlum()
        print("p1: ", str(blum.getP1()))
        print("p2: ", str(blum.getP2()))
        print("n: ", str(blum.getN()),end="\n\n")
        today = date.today()
        time.sleep(2)
        text = super(client, self).getPlayer().getStuffToSayElement(11) + "," + str(blum.getN())+ "," + str(today) +"," + super(client, self).getPlayer().getStuffToSayElement(23)
        print(super(client, self).getPlayer().getName() + ": ",text," -> ", dhKey.encryptMessage(text),end ="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(dhKey.encryptMessage(text)),end ="\n\n")#7
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(12),end ="\n\n")
        time.sleep(1)
        text = super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(12))#8
        print(super(client, self).getPlayer().getOtherOne() + ": ", text ,end ="\n\n")
        time.sleep(2)
        if(text != "Ok eseguiamo il controllo di n."):
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(13), end ="\n\n")
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(13)), end ="\n\n")#9
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(14), end ="\n\n")
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(14)), end ="\n\n")#10
            super(client, self).getConnection().closeConnection()
            sys.exit()
        print("Insieme Z_n: ", blum.getXValues(), "\n")
        print("Simboli di Jacobi per ogni elemento:", blum.getJacobiSymbols(), "\n")
        print(super(client, self).getPlayer().getName() + ": ", blumFairness.format(blum.getXSquaredValues()), end ="\n\n")
        time.sleep(1)
        bitsFromOtherOne = super(client, self).getConnection().clientSendReceiveMessage(blumFairness.format(blum.getXSquaredValues()))#9
        print(super(client, self).getPlayer().getOtherOne() + ": ", bitsFromOtherOne,end ="\n\n")
        time.sleep(2)
        blum.bitResponse(bitsFromOtherOne,4)
        print(super(client, self).getPlayer().getName() + ": ", blumFairness.format(blum.getBits()), end = "\n\n")
        time.sleep(1)
        super(client, self).getConnection().clientSendReceiveMessage(blumFairness.format(blum.getBits()))#10
        value = super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(15))
        print(super(client, self).getPlayer().getOtherOne() + ": ", value, end ="\n\n")#11
        if(value == super(client, self).getPlayer().getName() + " la verifica non è andata a buon fine!"):
            sys.exit()
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(15), end = "\n\n")
        time.sleep(1)
        encryptedMessageFromOtherOne = super(client, self).getConnection().clientSendReceiveMessage(" ")#12        
        print(super(client, self).getPlayer().getOtherOne() + ": ", encryptedMessageFromOtherOne," -> ", dhKey.decryptMessage(encryptedMessageFromOtherOne) , end = "\n\n")
        decryptedMessageFromOtherOne = dhKey.decryptMessage(encryptedMessageFromOtherOne)
        time.sleep(2)    
        resultValue = blum.syntaxControl(decryptedMessageFromOtherOne, 2)
        if(resultValue == 0):
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(17), end="\n\n")
            super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(17))#13
            time.sleep(1)
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(2), end="\n\n")
            time.sleep(1)
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(2)), end="\n\n")#14
            super(client, self).getConnection().closeConnection()
        elif(resultValue == 1):
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(18), end="\n\n")
            time.sleep(1)
            super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(18))#13
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(2), end="\n\n")
            time.sleep(1)
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(2)), end="\n\n")#14
            super(client, self).getConnection().closeConnection()
        elif(resultValue == 2):
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(19), end="\n\n")
            time.sleep(1)
            super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(19))#13
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(2), end="\n\n")
            time.sleep(1)
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(2)), end="\n\n")#14
            super(client, self).getConnection().closeConnection()
        time.sleep(2)
        blum.randomBits(11)
        myMessage = str(blum.getN()) + "," + blumFairness.format(blum.getXSquaredValues()) + "," + blumFairness.format(blum.getBits()) + "," + super(client, self).getPlayer().getStuffToSayElement(23)
        print(super(client, self).getPlayer().getName() + ": ", myMessage," -> ", dhKey.encryptMessage(myMessage),end="\n\n")
        time.sleep(1)
        myMessageEncrypted = dhKey.encryptMessage(myMessage)
        super(client, self).getConnection().clientSendReceiveMessage(myMessageEncrypted)#13
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(" "),end = "\n\n")#14
        time.sleep(2)
        messageFromOtherOne = super(client, self).getConnection().clientSendReceiveMessage(" ")#15
        print(super(client, self).getPlayer().getOtherOne() + ": ", messageFromOtherOne, end="\n\n")
        time.sleep(2)
        finalResult = blum.checkResult(messageFromOtherOne, super(client, self).getPlayer().getName())
        if(finalResult == False):
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(21)), end="\n\n")#16
            time.sleep(1)
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(21), end="\n\n")
        elif(finalResult == "Won"):
            print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(8), end="\n\n")
            time.sleep(1)
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(8)), end="\n\n")#16
        else:
            print(super(client, self).getPlayer().getName() + ": ",super(client, self).getPlayer().getStuffToSayElement(1), end="\n\n")          
            time.sleep(1)
            print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(1)), end="\n\n")#16
        time.sleep(2)
        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(2), end="\n\n")#16
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(2)), end="\n\n")#17
        super(client, self).getConnection().closeConnection()

    def rsaFairness(self):
        super(client, self).getConnection().setPort(10300)
        super(client, self).getConnection().createClientConnection()
        super(client, self).getPlayer().setMyRSA(myRSA())
        rsa = super(client, self).getPlayer().getMyRSA()
        if(not certificationAuthority.loadCA(rsa.getPubKey().n, rsa.getPubKey().e, super(client, self).getPlayer().getName())):
            super(client, self).getConnection().closeConnection()

        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(0), end="\n\n") #presentazioni
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(0)), end="\n\n") #1
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getChoice(), "*Cifrato*", end="\n\n") #primo scambio hash
        encryptedMessage = rsa.signature(super(client, self).getPlayer().getChoice())
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(encryptedMessage), end="\n\n") #2
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(6), end="\n\n")
        toSign = super(client, self).getConnection().clientSendReceiveMessage((super(client, self).getPlayer().getStuffToSayElement(6)))
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", toSign, end="\n\n") #3
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(3), end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(3)), end="\n\n") #4
        pubKeyOtherOneRAW = super(client, self).getConnection().clientSendReceiveMessage(rsa.getRawPubKey())
        keyOtherOne = rsa.setPubKeyFromRaw(pubKeyOtherOneRAW)
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", rsa.getPubKey(), end="\n\n")
        time.sleep(1)
        if(not certificationAuthority.checkCA(pubKeyOtherOneRAW, super(client, self).getPlayer().getOtherOne())):
            super(client, self).getConnection().closeConnection()
        else:
            print("signature check della chiave pubblica di " +  super(client, self).getPlayer().getOtherOne() + " via CA ha confermato l'identità del mittente  \n")

        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", keyOtherOne.getPubKey(), end="\n\n") #5
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", super(client, self).getPlayer().getStuffToSayElement(7), end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getStuffToSayElement(7)), end="\n\n") #6
        myChoiceEncrypted = rsa.encrypt(super(client, self).getPlayer().getChoice(), keyOtherOne.getPubKey())
        time.sleep(2)

        print(super(client, self).getPlayer().getName() + ": ", myChoiceEncrypted, end="\n\n")
        time.sleep(1)
        otherOneData =  super(client, self).getConnection().clientSendReceiveMessage(myChoiceEncrypted)
        print(super(client, self).getPlayer().getOtherOne() + ": ", otherOneData, end="\n\n") #7
        finalResult = rsa.decrypt(otherOneData)
        finalResult = finalResult.decode('utf8')
        time.sleep(2)

        print("Le estrazioni sono state: " , finalResult, end="\n\n")
        time.sleep(1)
        print(super(client, self).getPlayer().getName() + ": " , super(client, self).getPlayer().getRSAResult(finalResult, toSign, keyOtherOne.getPubKey()), end="\n\n")
        time.sleep(2)

        print(super(client, self).getPlayer().getOtherOne() + ": ", super(client, self).getConnection().clientSendReceiveMessage(super(client, self).getPlayer().getRSAResult(finalResult, toSign, keyOtherOne.getPubKey())), end="\n\n") #8
        super(client, self).getConnection().closeConnection()

        