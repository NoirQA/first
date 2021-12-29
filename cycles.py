import time

count = 0
while count < 1:
    count += 1
    print(count,'-- Hello')
    time.sleep(.500)

arr = [4,23,553,20,2324,50,23,90,23,1000,23]

for i in arr:
    dev_i = i % 10
    if dev_i == 0:
        print('i = ', i, 'dev_i', dev_i)
    # multiply_i = i * 10
    # print('Nubers',multiply_i)
    time.sleep(.500)

