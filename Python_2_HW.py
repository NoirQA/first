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
