"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств"""

import random

n = int(input('n= '))
numbers_n = [random.randint(0, 10) for _ in range(n)]
print(numbers_n)
m = int(input('m= '))
numbers_m = [random.randint(0, 10) for _ in range(m)]
print(numbers_m)
a = set(numbers_n)
b = set(numbers_m)
u = a.union(b)
print(f"Результат: {u}")
