"""Определить существование треугольника и его тип"""
a = float(input('vedita 1 storonu, zatem 2, zatem 3')) #если бы кто-то пользовался этим, ему было бы неудобно, исправь вывод информации на экран
b = float(input())
c = float(input())
if a == b == c :
    print('равносторонний')
elif a !=b and b!=c and (c!=a): #если ты разделяешь или связываешь условия, они должны быть в скобках, все!
    print('разносторонний')
else: print('равнобедренный')
