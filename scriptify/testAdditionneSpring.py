from springpython.aop import ProxyFactory
from ScriptifyInterceptor import ScriptifyInterceptor
from LibCalcul import LibCalcul

scriptFilename = "D:/testScriptify.py"
with open(scriptFilename, 'w') as script:
    script.write("from LibCalcul import LibCalcul\n\n")

factory = ProxyFactory()
factory.target = LibCalcul()
factory.interceptors.append(ScriptifyInterceptor(scriptFilename))
service = factory.getProxy()

nombre1 = service.getNombre(10)
chiffre1 = service.getChiffre(5)
nombre2 = service.additionne(nombre1, chiffre1)
service.printNombre(nombre2)