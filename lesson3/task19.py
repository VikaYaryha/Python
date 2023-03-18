'''Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]'''

import random

numbers = [random.randint(0, 11) for _ in range(5)]
print(numbers)
k = int(input('k= '))
numbers_new = []

for i in range(len(numbers)):
    numbers_new.append(numbers[-k + i])
print(numbers_new)

# for _ in range(k):
#     numbers.insert(0, numbers.pop()) - ВСТАВЛЯЕТ В ПЕРВУЮ ПОЗИЦИЮ ПОСЛЕДНИЙ ЭЛЕМЕНТ, удаляя его
# print(numbers)


# print(numbers[-k:] + numbers[:-k]) - срезы
