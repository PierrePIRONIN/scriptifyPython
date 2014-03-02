from LibCalcul import LibCalcul

if __name__ == '__main__':   
    
    datas = [(4,5), (3,2), (9,7)]
    
    for (int1,int2) in datas:
        Nombre1 = LibCalcul.getNombre(int1)
        Chiffre1 = LibCalcul.getChiffre(int2)
        Nombre2 = LibCalcul.additionne(Nombre1, Chiffre1)
        print Nombre2.toInt()