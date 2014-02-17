from springpython.aop import ProxyFactory
from LibCalcul import LibCalcul
from ScriptifyInterceptor import ScriptifyInterceptor

scriptFilename = "D:/testScriptify.py"
with open(scriptFilename, 'w') as script:
    script.write("from LibCalcul import LibCalcul\n\n")

factory = ProxyFactory()
factory.target = LibCalcul()
factory.interceptors.append(ScriptifyInterceptor(scriptFilename))
service = factory.getProxy()

#datas = [(4,5), (3,2), (9,7)]
#
#for (int1,int2) in datas:
nombre1 = service.getNombre(10)
chiffre1 = service.getChiffre(5)
nombre2 = service.additionne(nombre1, chiffre1)
service.printNombre(nombre2)