"""Определить существование треугольника и его тип"""
a = float(input('vedita 1 storonu, zatem 2, zatem 3'))
b = float(input())
c = float(input())
if a == b == c :
    print('равносторонний')
elif a !=b and b!=c and c!=a:
    print('разносторонний')
else: print('равнобедренный')
