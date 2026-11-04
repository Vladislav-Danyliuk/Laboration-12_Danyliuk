def _func(a):
    P = 4*a
    S = a*a
    all_S = S*6
    print("Повно площа поверхні куба = " , all_S , "см**2")
    Sb = P*a
    print("Площа бічної поверхні куба = " , Sb , "см**2")

def func_(a):
    S = a*a
    V = S*a
    print("Об'єм куба = " , V , "см**3")

a = int(input("Введіть довжину ребра куба: "))
_func(a)
func_(a)