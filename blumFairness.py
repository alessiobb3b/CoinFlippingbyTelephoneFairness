import random
from datetime import date
import time
from names import names
class blumFairness:

    def setP1(self, p):
        self.p1 = p
    
    def setP2(self, p):
        self.p2 = p
    
    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2
    
    def setN(self, n):
        self.n = n
    
    def getN(self):
        return self.n
    
    def addJacobiSymbol(self, symbol):
        self.jacobiSymbols.append(symbol)
    
    def getJacobiSymbols(self):
        return self.jacobiSymbols
    
    def addXValues(self, x):
        self.xValues.append(x)
    
    def getXValues(self):
        return self.xValues
    
    def addBits(self, bits):
        self.bits.append(bits)
    
    def getBits(self):
        return self.bits
    
    def getXValuesUsed(self):
        return self.xValuesUsed
    
    def getxUsedForTest(self):
        return self.xUsedForTest
    
    def addXSquaredValues(self, xSqrd):
        self.xSquaredValues.append(xSqrd)
    
    def getXSquaredValues(self):
        return self.xSquaredValues
    
    def addZN(self, zN):
        self.zN.append(zN)
    
    def getZN(self):
        return self.zN
    
    def addXValuesUsed(self, xUsed):
        self.xValuesUsed.append(xUsed)
    
    def __resetBits(self):
        self.bits = []
    
    def __resetXSquaredValue(self):
        self.xSquaredValues = []
    
    def __resetXValuesUsed(self):
        self.xUsedForTest = self.xValuesUsed
        self.xValuesUsed = []

    def __init__(self, n, section, nOfTries, setN = False):
        self.jacobiSymbols = []
        self.zN = []
        self.xValues = []
        self.xValuesUsed = []
        self.xSquaredValues = []
        self.bits = []
        self.xUsedForTest = []
        self.setN(n) if setN else self.setPAndN(n)
        self.euclide(section)
        self.jacobi()
        self.setSquareX(nOfTries)
    
    def blumFromScratch(self, n):
        return self.__init__(n, 0, 0)

    @staticmethod
    def randomWithNDigits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)

    def euclide(self, section):
        i = (int(self.getN()/2))
        while(len(self.getZN()) < section):
            temp = i
            _n = self.getN()
            while(temp > 0):
                r = _n % temp
                _n,temp = temp,r
            if(_n == 1):
                self.addZN(i)
            i = i + 1

    def setPAndN(self, _n):
        found = False
        while(not found):
            p = self.randomWithNDigits(_n)
            q = self.randomWithNDigits(_n)
            n = p*q
            if((p-3)%4 == 0 and (q-3)%4 == 0 and len(str(n)) == _n*2):
                found = True
                self.setP1(p)
                self.setP2(q)
                self.setN(n)


    def jacobi(self):
        zN = self.getZN()
        n = self.getN()
        res = []
        count1 = 0
        _count = 0
        for elem in zN:
            k = 0
            while(k < n+1):
                if(((k*k) - elem) % n == 0):
                    res.append(1)
                    count1 = count1 + 1
                    k = n + 1
                elif(k == n-1):
                    res.append(-1)
                    _count = _count + 1
                k = k + 1
        i = 0
        temp = 0
        if(count1 > _count):
            minimal = _count
            ref = -1
        else:
            minimal = count1
            ref = 1
        while(i < len(zN)):
            if(temp < minimal and res[i] != ref):
                temp += 1
                self.addJacobiSymbol(res[i])
                self.addXValues(zN[i])
            elif(res[i] == ref):
                self.addJacobiSymbol(res[i])
                self.addXValues(zN[i])
            i += 1

    def checkN(self):
        if((self.getN()-1) % 4 == 0):
            return True
        else:
            return False
        
    def setSquareX(self, times):
        n = self.getN()
        values = self.getXValues()
        self.__resetXSquaredValue()
        self.__resetXValuesUsed()
        i = 0
        while(i < times):
            j = random.randint(0,len(values)-1)
            if((values[j] not in self.getXValuesUsed()) and (values[j] not in self.getxUsedForTest())):
                self.addXSquaredValues((values[j]**2) % n)
                self.addXValuesUsed(values[j])
                i += 1

    def randomBits(self, times):
        self.__resetBits()
        values = [-1,1]
        i = 0
        while(i < times):
            j = random.randint(0,1)
            self.addBits(values[j])
            i += 1

    def checkResult(self, x, whois):
        x = self.__listToIntlist(x) if isinstance(x, str) else x
        count1 = 0
        countother = 0
        values = self.getXValues()
        n = self.getN()
        squared = self.getXSquaredValues()
        jacobi = self.getJacobiSymbols()
        bits = self.getBits()
        i = 0
        while(i < len(x)):
            temp = (x[i]**2) % n
            if(temp != squared[i]):
                return False
            i += 1
        i = 0
        tempJacobiValues = []
        while(i < len(x)):
            j = 0
            found = False
            while(j < len(values)):
                if(x[i] == values[j]):
                    tempJacobiValues.append(jacobi[j])
                    found = True
                    if(jacobi[j] == bits[i]):
                        count1 += 1
                    else:
                        countother += 1
                j += 1
            if(not found):
                return found
            i += 1
        self.__recap(x, tempJacobiValues)
        if(whois == names().getServerName()):
            print("*Hai totalizzato: " + str(countother) + " punti*", end="\n\n")
            if(countother > count1):
                return "Won"
            else:
                return "Lost"
        else:
            print("*Hai totalizzato: " + str(count1) + " punti*", end="\n\n")
            if(countother > count1):
                return "Lost"
            else:
                return "Won"

    def controlBits(self, x):
        values = self.__listToIntlist(x)
        i = 0
        while(i < len(values)):
            if(values[i] not in self.getXValues()):
                return False
            j = 0
            while(j < len(self.getXValues())):
                if(values[i] == self.getXValues()[j]):
                    if(self.getJacobiSymbols()[j] != self.getBits()[i]):
                        return False
                j += 1
            i += 1
        return True

    def bitResponse(self, bits, times):
        bits = self.__listToIntlist(bits)
        i = 0
        used = []
        while(i < times):
            rand = random.randint(0,len(self.getXValues())-1)
            temp = self.getXValues()[rand]
            if(self.getJacobiSymbols()[rand] == bits[i] and (temp not in self.getBits())):
                used.append(temp)
                self.addBits(temp)
                i += 1


    def __listToIntlist(self, value):
        value = value.split(",")
        res =[]
        for elem in value:
            res.append(int(elem))
        return res
    
    @staticmethod
    def format(values):
        res = ""
        for elem in values:
            res += str(elem) + ","
        return res[:-1]

    def syntaxControl(self, decryptedMessageFromOtherOne, protocolPhase, tries = 0):
        decryptedMessageFromOtherOne = decryptedMessageFromOtherOne.split(",")
        if(protocolPhase == 2):
            self.__resetXSquaredValue()
            if(decryptedMessageFromOtherOne[1] == str(date.today())):
                if(decryptedMessageFromOtherOne[len(decryptedMessageFromOtherOne)-1] == " firmato " + names().getServerName() + "."):
                    if(int(decryptedMessageFromOtherOne[0]) == self.getN()):
                        i = 2
                        while(i < (len(decryptedMessageFromOtherOne)-1)):
                            self.addXSquaredValues(int(decryptedMessageFromOtherOne[i]))
                            i += 1
                        return 10
                    else:
                        return 2
                else:
                    return 1
            else:
                return 0
        elif(protocolPhase == 3):
            xsqrd = self.getXSquaredValues()
            self.__resetBits()
            if(len(decryptedMessageFromOtherOne) < 10):
                return 1
            if(decryptedMessageFromOtherOne[len(decryptedMessageFromOtherOne)-1] == " firmato " + names().getClientName() + "."):
                if(int(decryptedMessageFromOtherOne[0]) == self.getN()):
                    i = 1
                    while(i < (tries + 1)):
                        if(int(decryptedMessageFromOtherOne[i]) != xsqrd[i-1]):
                            return 3
                        i += 1
                    while(i < (len(decryptedMessageFromOtherOne)-1)):
                        self.addBits(int(decryptedMessageFromOtherOne[i]))
                        i += 1
                    return 10
                else:
                    return 2
            else:
                return 0
    
    @staticmethod
    def createFromRaw(decryptedMessageFromOtherOne, section, nOfTries, setN):
        decryptedMessageFromOtherOne = decryptedMessageFromOtherOne.split(",")
        if(decryptedMessageFromOtherOne[2] == str(date.today())):
            if(decryptedMessageFromOtherOne[3] == " firmato " + names().getClientName() + "."):
                blum = blumFairness(int(decryptedMessageFromOtherOne[1]), section, nOfTries, setN)
                if(blum.checkN()):
                    return blum
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    
    def __recap(self, x, jacobiSymbols):
        print("****SITUAZIONE FINALE****", end="\n\n")
        print("X^2 mod n : ", self.getXSquaredValues(), end="\n\n")
        print("X: ", x, end="\n\n")
        print("Simboli reali:          ", jacobiSymbols, end="\n\n")
        print("Bit ipotizzati da", names().getClientName(), ": ", self.getBits(), end="\n\n")
        print("*************************", end="\n\n")
        
                
                

            



