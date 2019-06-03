"""Решить квадратное уравнение"""
#ax^2+bx+c=0
from math import sqrt #as sqrt лишнее, as используется лишь, для перееименования
print('ax^2+bx+c=0, введите a-->b-->c')
a = float(input())
b = float(input())
c = float(input())
#d = float() строчка не нужна, в python тип переменной задается автоматически
d = b**2 - (4*a*c)

'''
Исправь If - неверное условие https://www.berdov.com/docs/equation/quadratic_equations/
'''
if d < 0:
    print('нет корней')
elif d == 1:
    print('1 корень')
    print((-b + sqrt(d))/2)
elif d > 1:
    print('2 корня')
    print((-b + sqrt(d)) / 2)
    print((-b - sqrt(d)) / 2)


