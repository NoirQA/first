import math

item_1 = 23
item_2 = 73
result_sum = item_1 + item_2
print('result_sum =', result_sum)

result_subtr = item_2 - item_1
print('result_subtr =', result_subtr)

result_multi = item_1 * item_2
print('result_multi =', result_multi)

result_exp = item_1 ** item_2
print('result_exp =', result_exp)

result_m_exp = math.pow(item_1, item_2)
print('result_m_exp =', result_m_exp)

result_s_root = item_2 ** (0.5)
print('Квадратный корень из result_s_root ' + str(item_2) + ' это ' + str(result_s_root))

result_s_m_root = math.sqrt(item_2)
print('Квадратный корень из result_s_m_root ' + str(item_2) + ' это ' + str(result_s_m_root), 'math.sqrt')

# 17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя
# библиотеку math используя метод pow.
#  Или я чего то не понял или это задание выполнено в строке 17 (поправьте если я ошибаюсь)

item_1 = 93 # Odd
item_2 = 20 # Even

result_division = item_1 / item_2
print('result_division = ', result_division)

result_m_floor = math.floor(result_division)
print('результат округление', result_division,'в меньшую сторону =',result_m_floor)

result_m_ceil = math.ceil(result_division)
print('результат округление', result_division,'в большую сторону =',result_m_ceil)

result_int = int(result_division)
print('результат округление', result_division,'явным приведением "int" =',result_int)

result_no_division_loss = item_1 // item_2
print('результат деления ', item_1, 'на',item_2, 'без отстатка =',result_no_division_loss)

result_division_loss2 = item_1 % item_2
print('отстаток от деления',item_1, "%",item_2,'Равен',result_division_loss2)

item_3 = 5
# Сложение с присвоением
item_3 += 10
print(item_3)
# Вычитание с присвоением
item_3 -= 5
print(item_3)
# Умножение с присвоением
item_3 *= 3
print(item_3)
# Деление с присвоением
item_3 /= 2
print(item_3)
# Возведение в степень с присвоением
item_3 **= 2
print(item_3)
# Квадратный корень с присовением
item_3 **= 0.5
print(item_3)
# Деление без остатка с присвоением
item_3 %= item_3
print(item_3)

b_item_t = True
b_item_f = False
b_item_relult_sum = b_item_f + b_item_t
print('Результат сложения =',b_item_relult_sum )

b_item_relult_subtr = b_item_t - b_item_f
print('Результат вычетания =',b_item_relult_subtr)

b_item_relult_multi = b_item_t * b_item_f
print('Результат умножения =',b_item_relult_multi)

try:
    b_item_relult_division = b_item_t / b_item_f
except ZeroDivisionError:
    b_item_relult_division = 0
print('Результат деления', b_item_relult_division)

b_item_1_int = int(b_item_t)
print(b_item_1_int)

b_item_2_int = int(b_item_f)
print(b_item_2_int)