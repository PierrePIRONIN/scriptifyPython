class Nombre:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def toInt(self):
        return self.nombre
    
    def printOut(self):
        print self.toInt()