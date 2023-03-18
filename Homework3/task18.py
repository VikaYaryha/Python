"""Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В
последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
 6
-> 5"""

import random

n = int(input('n= '))
numbers = [random.randint(0, 10) for _ in range(n)]
dif = float('inf')
m = numbers[0]
print(numbers)
x = int(input('x= '))
for i in range(n):
    if abs(x - numbers[i]) < dif:
        dif = abs(x - numbers[i])
        m = numbers[i]
print(m)