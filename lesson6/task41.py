"""Дан массив, состоящий из целых чисел. Напишите программу, 
которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел."""


count = 0
n = int(input('len='))
list_1 = [int(input('число= ')) for _ in range(n)]

#или
# for _ in range (n):
#     a = int(input('n='))
#     list_1.append(a)
    
print (list_1)

for i in range(1, n-1):
    if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]:
        count+=1
print(f"Ответ: {count}")