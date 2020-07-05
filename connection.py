import socket
from errorMessage import errorMessage
from names import names
class connection:

    def setAddress(self, address):
        try:
            socket.inet_aton(address)
        except socket.error:
            errorMessage.printError(3)
        self.address = address
    
    def setPort(self, port):
        self.port = port
    
    def setSocket(self, socket):
        self.socket = socket
    
    def __init__(self, address):
        self.setAddress(address)
    
    def getAddress(self):
        return self.address
    
    def getPort(self):
        return self.port
    
    def getSocket(self):
        return self.socket
    

    def createClientConnection(self):
        def get_constants(prefix):
            """Create a dictionary mapping socket module constants to their names."""
            return dict( (getattr(socket, n), n)
                    for n in dir(socket)
                    if n.startswith(prefix)
                    )

        families = get_constants('AF_')
        types = get_constants('SOCK_')
        protocols = get_constants('IPPROTO_')

        # Create a TCP/IP socket
        print("In attesa di una connessione con "  + names().getServerName() + "...", end = "\n\n")
        self.setSocket(socket.create_connection((self.getAddress(), self.getPort())))


    def clientSendReceiveMessage(self, msg):
        try:
            msg=msg.encode()
        except:
            pass
        self.getSocket().sendall(msg)
        data = self.getSocket().recv(10000)
        try:
            data = data.decode()
        except:
            pass
        return data

    def closeConnection(self):
        self.getSocket().close()

    def serverCreateConnection(self):
        self.setSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        server_address = (self.getAddress(), self.getPort())
        print("In attesa di una connessione con " + names().getClientName() + "...", end = "\n\n")
        self.getSocket().bind(server_address)
        self.getSocket().listen(4)
        connected, client_address = self.getSocket().accept()
        self.setSocket(connected)

    def serverSendReceiveMessage(self, msg):
        data = ''
        while(data == ''):
            try:
                data = self.getSocket().recv(10000)
                try:
                    data = data.decode()
                except:
                    pass
                try:
                    msg = msg.encode()
                except:
                    pass
                self.getSocket().sendall(msg)
                return data
            finally:
                pass