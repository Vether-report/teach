"""Определить нечетное число
Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.
"""
from random import random
a = int(random() * 10)
b = int(random() * 10)
if a%2 and b%2 or a%2==0 and b%2==0:
 b += 1
print(a,b)
if a%2:
        print(a)
else:
        print(b)