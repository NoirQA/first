# Переменная String
myName = 'Eugne'
print('Тип переменой: ', type(myName), myName)

# Переменная Integer
myAge = 38
print('Тип переменой: ', type(myAge), myAge)

# Переменная Float
myTemp = 36.6
print('Тип переменой: ', type(myTemp), myTemp)

# Переменная Bytes
myAgeBytes = bytes(38)
print('Тип переменой: ', type(myAgeBytes), myAgeBytes)

# Переменная Tuple (Нельзя добавить элемент, нельзя удалить элемент, )
myFamaly = ("Olga", "Plato", "Sofi")
print('Тип переменой: ', type(myFamaly), myFamaly)

# Переменная List
myDocList = ["Passport", "Driver's license", "Deditation insurance"]
print('Тип переменой: ', type(myDocList), myDocList)

# Переменная set (элементы множества всегда уникальны, неупорядоченная коллекция. Для создания пустого множества
# нужно непосредственно использовать set())
mySets = {1, 1, 2, 3, 3, 2}
print('Тип переменой: ', type(mySets), mySets)

#   Переменная frozenset //
myLib = frozenset('П у ш к и')
print('Тип переменой: ', type(myLib), myLib)

# Переменная Dict (Словать)

myDict = {'hello': 'Привет', 'bye': 'Пока'}
print('Тип переменой: ', type(myDict), myDict)

# Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль. +
strTextOne = 'Это '
strTextTwo = 'Восхитительно'
strTextThree = strTextOne + strTextTwo
print('Pythe', strTextThree)

# Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
digOne = 635
digTwo = 923
total = digOne + digTwo
print('Результат сложения 635 + 923 =', total)
point13 = digOne / digTwo
print('Результат деления  635 / 923 =', point13)
point14 = digOne * digTwo
print('Результат умножения 635 * 923 =', point14)
digThree = 9
digFour = 3
point15 = digThree / digFour
print('Результат деления 9 / 3 =', point15)
point16 = digTwo % digThree
print('Остаток от деления =', point16)
print((7 + 12) * 3 + 7 * 4 - 44 / 2 * 0.4)
