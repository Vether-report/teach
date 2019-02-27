"""Выведите случайное количество раз фразу: “Привет!”"""
from random import randint
u = int(randint(1,10))
i = 1
for i in range(u):
    print('привет')