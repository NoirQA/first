# Переменная String
myName = 'Eugne'
print(('Тип переменой: '),type(myName),myName)

# Переменная Integer
myAge = 38
print(('Тип переменой: '),type(myAge),myAge)

# Переменная Float
myTemp = 36.6
print(('Тип переменой: '),type(myTemp),myTemp)

# Переменная Bytes
myAgeBytes = bytes(38)
print(('Тип переменой: '),type(myAgeBytes),myAgeBytes)

# Переменная Tuple (Нельзя добавить элемент, нельзя удалить элемент, )
myFamaly = ("Olga", "Plato", "Sofi")
print(('Тип переменой: '),type(myFamaly),myFamaly)

# Переменная List
myDocList = ["Passport", "Driver's license", "Deditation insurance"]
print(('Тип переменой: '),type(myDocList), myDocList)

# Переменная set (элементы множества всегда уникальны, неупорядоченная коллекция. Для создания пустого множества нужно непосредственно использовать set())
mySets = {1, 1, 2, 3, 3, 2}
print(('Тип переменой: '),type(mySets),mySets)

#   Переменная frozenset //
myLib = frozenset('П у ш к и')
print(('Тип переменой: '),type(myLib),myLib)

# Переменная Dict (Словать)

myDict = {'hello':'Привет', 'bye':'Пока'}
print(('Тип переменой: '),type(myDict),myDict)

strTextOne = 'Это '
strTextTwo = 'Восхитительно'
strTextThree = strTextOne + strTextTwo
print('Pythe',(strTextThree))