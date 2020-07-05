import requests
class certificationAuthority:
    @staticmethod
    def loadCA(n, e, whoami):
         url = 'http://192.168.1.10/Fairness/Check.php'
         msg = str(n) + ";" + str(e) + ',' + whoami
         myobj = {'value': msg}
         x = requests.post(url, data = myobj, timeout = 5)
         val = x.text
         if(val[:len(val)-2] != "CARICATO"):
             return False
         else:
             return True

    @staticmethod
    def checkCA(temp, otn):
         url = 'http://192.168.1.10/Fairness/Load.php'
         value = temp.split(',')
         msg = value[0] + ";" + value[1] + ',' + otn
         myobj = {'value': msg}
         x = requests.post(url, data = myobj, timeout = 5)
         val = x.text
         if(val != 'VERIFICATO'):
             return False
         else:
             return True