class clientServerModel:
    
    def setPlayer(self, player):
        self.player = player
    
    def getPlayer(self):
        return self.player
    
    def setConnection(self, connection):
        self.connection = connection
    
    def getConnection(self):
        return self.connection
    
    def __init__(self, player, connection):
        self.setPlayer(player)
        self.setConnection(connection)
        
    