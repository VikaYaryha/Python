"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего
на грядке растет N кустов.Эти кусты обладают разной урожайностью, 
поэтому ко времени сбора на них выросло различное число 
ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора 
черники. Эта система состоит из управляющего модуля и нескольких с
обирающих модулей. Собирающий модуль за один заход, находясь 
непосредственно перед некоторым кустом, собирает ягоды с этого 
куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, находясь 
перед некоторым кустом заданной во входном файле грядки."""

import random

n = int(input('Количество кустов черники '))
berry = [random.randint(0, 1000) for _ in range(n)]
print(berry)
max = float('-inf')
for i in range(n-2):
    if ((berry[i] + berry[i + 1] + berry[i + 2]) > max):
        max = berry[i] + berry[i + 1] + berry[i + 2]
    if ((berry[0] + berry[n - 1] + berry[n - 2]) > max):
        max = berry[0] + berry[n - 1] + berry[n - 2]
    if ((berry[0] + berry[1] + berry[n - 1]) > max):
        max = berry[0] + berry[1] + berry[n - 1]
print(max)