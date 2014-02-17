from Nombre import Nombre
from Chiffre import Chiffre

class LibCalcul:
    @staticmethod
    def getNombre(nombre):
#         print "getNombre avec", nombre
        return Nombre(nombre)
    
    @staticmethod
    def getChiffre(chiffre):
#         print "getChiffre avec", chiffre
        return Chiffre(chiffre)
    
    @staticmethod
    def additionne(nombre, chiffre):
#         print "additionne", nombre, chiffre
        return Nombre(nombre.toInt() + chiffre.toInt())