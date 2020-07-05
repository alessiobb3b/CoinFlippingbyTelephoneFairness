from argParser import argParser
from player import player
from connection import connection
from client import client
from server import server
from names import names
import sys

def text_show(): #Funzione per mostrare l'ASCII Art di presentazione
    fairness_draw = open('intro.txt','r')
    print(fairness_draw.read())
    print('\n')
    
def main():
    text_show()

    arg = argParser()
    value = arg.checkArgs()
    itsMe = client(player(names().getClientName(), value, True), connection(arg.getArgs().__dict__["address"])) if arg.getArgs().__dict__["client"] else server(player(names().getServerName(), value, False), connection(arg.getArgs().__dict__["address"]))

    while(True):
        value = input("Ciao " + itsMe.getPlayer().getName() + ", quale modalità di connessione desideri provare? : \n1) No-Fairness \n2) Blum-Fairness \n3) RSA-Fairness\n")
        if(value == "1"):
            itsMe.noFairness()
        elif(value == "2"):
           itsMe.blumFairness()
        elif(value == "3"):
           itsMe.rsaFairness()
        else:
            print("Valore non valido. RIprovare!", end="\n\n")
        


if __name__ == "__main__":
    main()
        

