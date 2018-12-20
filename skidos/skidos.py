def pir(a1):
    summ=a1
    if (summ < 500):
        print('недостаточная сумма покупки', summ)

    if (summ >= 500)and(summ<1000):
        summ = summ * 0.97
        print(summ)

    if (summ>=1000):
        summ = summ * 0.95
        print(summ)

#main
summ=int(input('введите сумму покупки:  '))

#print(type(summ))
#while summ!=0: #циул с условием пока.....
   #pir(summ)
    #summ = int(input('введите сумму покупки:  '))

for x in range(0,2,1): #цикл
    print(x,':')
    pir(summ)
    summ = int(input('введите сумму покупки:  '))