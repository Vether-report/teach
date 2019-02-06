"""Какой координатной четверти принадлежит точка?"""
a = float(input('vedita x, a zatem y'))
b = float(input())
if a > 0 and b > 0 :
    print('1 четверть')
elif a < 0 and b > 0 :
    print('2 четверть')
elif a < 0 and b < 0:
    print('3 четверть')
elif a > 0 and b < 0:
    print('4 четверть')

