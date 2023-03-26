"""Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные."""

otmetki = [4, 5, 3, 4, 5]
# for i, num in enumerate(otmetki):
#     if num == 5:
#         otmetki[i] = 2
#     elif num == 4:
#         otmetki[i] = 1
# print (*otmetki)

otmetki_1 = [(i-3) if i > 3 else i for i in otmetki]
print (otmetki_1)