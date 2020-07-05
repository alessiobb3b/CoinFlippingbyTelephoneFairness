class diffieHelman:

    def __init__(self, publicKey1, publicKey2, privateKey):
        self.publicKey1 = publicKey1
        self.publicKey2 = publicKey2
        self.privateKey = privateKey
        self.fullKey = None
        
    def generatePartialKey(self):
        partialKey = self.publicKey1**self.privateKey
        partialKey = partialKey%self.publicKey2
        return partialKey
    
    def generateFullKey(self, partialKeyR):
        fullKey = partialKeyR**self.privateKey
        fullKey = fullKey%self.publicKey2
        self.fullKey = fullKey
    
    def encryptMessage(self, message):
        encryptedMessage = ""
        key = self.fullKey
        for c in message:
            encryptedMessage += chr(ord(c)+key)
        return encryptedMessage
    
    def decryptMessage(self, encryptedMessage):
        decryptedMessage = ""
        key = self.fullKey
        for c in encryptedMessage:
            decryptedMessage += chr(ord(c)-key)
        return decryptedMessage
    
    def getPQRaw(self):
        return str(self.publicKey1) + " " + str(self.publicKey2)
        