from Nombre import Nombre
from Chiffre import Chiffre

class LibCalcul: 
    @staticmethod
    def getNombre(nombre):
        return Nombre(nombre)
    
    @staticmethod
    def getChiffre(chiffre):
        return Chiffre(chiffre)
    
    @staticmethod
    def additionne(nombre, chiffre):
        return Nombre(nombre.toInt() + chiffre.toInt())
    
    @staticmethod
    def printNombre(nombre):
        print nombre.toInt()