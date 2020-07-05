import rsa
class myRSA:
    
    def setPubKey(self, pubKey):
        self.pubKey = pubKey
    
    def setPubKeyFromRaw(self,values):
        keys = values.split(',')
        n = int(keys[0])
        e = int(keys[1])
        nRSA = myRSA()
        nRSA.setPubKey(rsa.PublicKey(n,e))
        return nRSA
    
    def getRawPubKey(self):
        return str(self.getPubKey().n) + "," + str(self.getPubKey().e)

    def getPubKey(self):
        return self.pubKey

    def setPrivKey(self, privKey):
        self.privKey = privKey
    
    def getPrivKey(self):
        return self.privKey

    def setPair(self, key):
        (self.pubKey, self.privKey) = key

    def __init__(self):
        self.setPair(rsa.newkeys(1024))

    def encrypt(self, message, pubkey):
        message = message.encode('utf8')
        return rsa.encrypt(message, pubkey)

    def decrypt(self, message):
        message = rsa.decrypt(message,self.getPrivKey())
        return message

    def signature(self, message):
        message = message.encode('utf8')
        return rsa.sign(message, self.getPrivKey(), 'SHA-1')

    def verifySignature(self, message, signature, pubKeyOtherOne):
        res = False
        message = message.encode('utf8')
        try:
            res = rsa.verify(message, signature, pubKeyOtherOne)
        except:
            res = False
        return res