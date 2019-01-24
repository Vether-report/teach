"""Определить нечетное число
Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.
"""
from random import randint as rd
a,b = [int(rd(1,1000))*x for x in range(1,3)]
print(a,b)
a = int(rd(1,1000)) * 2
b = int(rd(1,1000)) * 3
print(a,b)
if a%2==0:
    print(b)
else:
    print(a)