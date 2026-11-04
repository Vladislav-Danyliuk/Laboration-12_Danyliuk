# потрібно щоб індекси у повідомленні мінялись місцями, парні з парними н.д.: [2]->[8] + непарні з непарними н.д.: [1]->[5]
#a = list( input( massage ) ) , b = перемішати
import random

def func(a):
    a = list( input("Введіть повідомлення: \n > ") )
    a1 = len(a)
    A = list()
    print(a1)
    for b in range(a1//2):
        b = a[ random.randrange(0 , a1 , 2) ]
        A.append(b)
    for b in range(a1//2):
        i =  random.randint(0 , a1) 
        b = a[i]
        if i%2 != 0:
            A.append(b)
        elif i%2 == 0:
            not A.append(b)
    print("\n" , A)

a = str()
func(a)