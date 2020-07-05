import argparse
import random
from errorMessage import errorMessage
import sys
class argParser:

    def setParser(self, value):
        self.parser = value
    
    def setArgs(self, value):
        self.parsedArgs = value

    def parse(self):
        self.parser.add_argument("-c", "--client", action='store_true', help="Set the main as client")
        self.parser.add_argument("-s", "--server", action='store_true', help="Set the client as server")
        self.parser.add_argument("-a", "--address", help="IP address of the other side", type = str)
        self.parser.add_argument("-ht", "--headortail", help="[OPTIONAL]You can choose, only if you're the client, head or tail", type = str)
    
    def __init__(self):
        self.setParser(argparse.ArgumentParser())
        self.parse()
        self.setArgs(self.parser.parse_args())

    def getArgs(self):
        return self.parser.parse_args()
    
    def checkArgs(self):
        myArgs = self.getArgs()
        if (myArgs.__dict__["client"] and myArgs.__dict__["server"]) or (not myArgs.__dict__["client"] and not myArgs.__dict__["server"]):
            errorMessage.printError(1)
        if (not myArgs.__dict__["address"]):
            errorMessage.printError(2)
        if(not myArgs.__dict__["headortail"] or ((myArgs.__dict__["headortail"].lower() != "testa" and myArgs.__dict__["headortail"].lower() != "croce"))):
            value = "testa" if random.randrange(0,100) >= 50 else "croce"
        else:
            value = myArgs.__dict__["headortail"]
        return value
