from springpython.aop import ProxyFactory
from LibCalcul import LibCalcul
from ScriptifyInterceptor import ScriptifyInterceptor

factory = ProxyFactory()
factory.target = LibCalcul()
factory.interceptors.append(ScriptifyInterceptor())
service = factory.getProxy()

datas = [(4,5), (3,2), (9,7)]

for (int1,int2) in datas:
    nombre1 = service.getNombre(int1)
    chiffre1 = service.getChiffre(int2)
    nombre2 = service.additionne(nombre1, chiffre1)
    print nombre2.toInt()