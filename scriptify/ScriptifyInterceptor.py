from springpython.aop import MethodInterceptor

class ScriptifyInterceptor(MethodInterceptor):
    _sessionIds = {}
    _sessionIdGenerated = {}
    
    def __init__(self, outputFilename):
        self._outputFilename = outputFilename
    
    def getClassNameForObject(self, objectTarget):
        return objectTarget.__class__.__name__
    
    def getGeneratedIdForObject(self, objectTarget):
        objectClassname = self.getClassNameForObject(objectTarget)
        if not objectClassname in ScriptifyInterceptor._sessionIdGenerated.keys():
            ScriptifyInterceptor._sessionIdGenerated[objectClassname] = 0
        ScriptifyInterceptor._sessionIdGenerated[objectClassname] += 1
        return ScriptifyInterceptor._sessionIdGenerated[objectClassname]

    def getIdForObject(self, objectTarget):
        objectId = id(objectTarget)
        if not objectId in ScriptifyInterceptor._sessionIds.keys():
            ScriptifyInterceptor._sessionIds[objectId] = self.getGeneratedIdForObject(objectTarget)
        return ScriptifyInterceptor._sessionIds[objectId]

    def getVariableForObject(self, objectTarget):
        return self.getClassNameForObject(objectTarget).lower() + "_" + str(self.getIdForObject(objectTarget))

    def invoke(self, invocation):
        lstArgs = []
        for arg in invocation.args:
            if not isinstance(arg, int):
                lstArgs.append(self.getVariableForObject(arg))
            else:
                lstArgs.append(str(arg))
        result = self.getClassNameForObject(invocation.instance) + "." + invocation.method_name + "(" + str(", ").join(lstArgs) + ")"
        objectReturned = invocation.proceed()
        if objectReturned:
            result = self.getVariableForObject(objectReturned) + " = " +  result
        with open(self._outputFilename, 'a') as script:
            script.write(result+"\n")
        return objectReturned