# Переменная String
myName = 'Eugne'
print(type(myName),myName)

# Переменная Integer
myAge = 38
print(type(myAge),myAge)

# Переменная Float
myTemp = 36.6
print(type(myTemp),myTemp)

# Переменная Bytes
myAgeBytes = bytes(38)
print(type(myAgeBytes),myAgeBytes)

# Переменная Tuple (Нельзя добавить элемент, нельзя удалить элемент, )
myFamaly = ("Olga", "Plato", "Sofi")
print(type(myFamaly),myFamaly)

# Переменная List
myDocList = ["Passport", "Driver's license", "Deditation insurance"]
print(type(myDocList), myDocList)

# Переменная set (элементы множества всегда уникальны, неупорядоченная коллекция. Для создания пустого множества нужно непосредственно использовать set())
mySets = {1, 1, 2, 3, 3, 2}
print(type(mySets),mySets)

#   Переменная frozenset //
myLib = frozenset('П у ш к и')
print(type(myLib),myLib)

# Переменная Dict (Словать)

myDict = {'hello':'Привет', 'bye':'Пока'}
print(type(myDict),myDict)