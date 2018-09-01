import sys

INDENT = "    " 

def getTestClassName(className):
	return className + "Test";

def getMockName(paramName):
	return paramName+"Mock_"

def getMockMemberDefinition(interfaceName, paramName):
	return "private " + interfaceName + " " + paramName +"Mock_;\n";

def getMockAssign(interfaceName, paramName):
	return INDENT + INDENT + getMockName(paramName) + "= new Substitue.For<" + interfaceName + ">();\n"


constructorSignature = sys.argv[1]
splitSignature = constructorSignature.split("(")
className = splitSignature[0]
constructorParams = splitSignature[1].translate({ord(c): None for c in ');\n'})
splitParams = constructorParams.split(", ")

print("ClassName:" + className)
argCount = len(splitParams);
print("Number of Parameters:" + str(len(splitParams)))


memberDefLines = ""
instantiationLines = ""

for i in range(argCount):
	print("ArgIndex:" + str(i))
	entry = splitParams[i].strip()
	splitEntry = entry.split(" ")
	typeName = splitEntry[0]
	paramName = splitEntry[1]
	print("Class Name:" + typeName)
	print("Parameter Name:" + typeName)
	if(typeName[0] == 'I'):
		print("Type: Interface")
		memberDefLines += (INDENT+ getMockMemberDefinition(typeName, paramName))
		instantiationLines += getMockAssign(typeName, paramName)
	else:
		print("Type: Non-Interface")

print("--------------------------------------- mockgen");
print(getTestClassName(className) + "{\n" )
print(memberDefLines)
print(INDENT + "[SetUp]")
print(INDENT + "public void Setup(){\n")
print(instantiationLines)
print(INDENT + "}")
print("}\n")
