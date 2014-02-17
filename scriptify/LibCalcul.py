from Nombre import Nombre
from Chiffre import Chiffre

class LibCalcul:
    def getNombre(self, nombre):
#         print "getNombre avec", nombre
        return Nombre(nombre)
    
    def getChiffre(self, chiffre):
#         print "getChiffre avec", chiffre
        return Chiffre(chiffre)
    
    def additionne(self, nombre, chiffre):
#         print "additionne", nombre, chiffre
        return Nombre(nombre.toInt() + chiffre.toInt())