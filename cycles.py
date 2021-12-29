import time

curr = 'USD'
cuss_rate = 76.54

while True:

    usd_input = input('Enter USD: ')
    usd_rub = float(usd_input) * cuss_rate

    print('You enter USD:',usd_input)
    print('Your RUS:',usd_rub)




# count = 0
# while count < 1:
#     count += 1
#     print(count,'-- Hello')
#     time.sleep(.500)
#
# arr = [4,23,553,20,2324,50,23,90,23,1000,23]
#
# for i in arr:
#     print('i =', i)
#     if i == 23:
#         continue
#     print('Hello', i * 10)
#     print('--------------')
#     # multiply_i = i * 10
#     # print('Nubers',multiply_i)
#     time.sleep(.500)

