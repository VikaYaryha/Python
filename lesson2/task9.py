""". По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while"""

"""n = int(input("Введите n "))
i = 1
result = 1
while i<= n:
    result*=i
    i+=1
print (f"{n}! = {result}")"""

n = int(input())
i = 1
while n > 1:
    i *= n
    n -= 1
print(i)