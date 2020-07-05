from errorMessage import errorMessage
class names():

    def __init__(self):
        primes = open("WhoTheyAre.txt",'r')
        primes = primes.readlines()
        self.setClientName(primes[0].rstrip())
        self.setServerName(primes[1].rstrip())
        if(self.getClientName() == self.getServerName()):
            errorMessage.printError(4)

    def setClientName(self, client):
        self.client = client
    
    def setServerName(self, server):
        self.server = server

    def getClientName(self):
        return self.client
    
    def getServerName(self):
        return self.server
