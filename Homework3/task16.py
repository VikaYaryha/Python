"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
3
-> 1"""

import random

n = int(input('n= '))
numbers = [random.randint(0, 10) for _ in range(n)]
count = 0
print(numbers)
x = int(input('x= '))
for i in numbers:
    if i == x:
        count+=1
print(count)