import sys
class errorMessage:
    @staticmethod
    def printError(value):
        switcher = {
            1: "Attenzione! Non è stata inserita la flag -c o -s oppure i flag sono stati inseriti insieme",
            2: "Attenzione! Non è stato inserito un indirizzo ip al quale connettersi",
            3: "Indirizzo ip non valido",
            4: "Attenzione! Sono stati inseriti due nomi identici per client e server",
            5: "",
        }
        sys.exit(switcher.get(value))
