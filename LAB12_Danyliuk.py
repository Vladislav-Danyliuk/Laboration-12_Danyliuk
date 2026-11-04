print("- - Завдання 1.1 - -")
def func(a , b):
    c = 1
    i1 = list()
    for i in range(a):
        i = a%c ==0
        if i == True:
            i1.append(c)
        #print(i , " < > " , c)
        c += 1
    
    f = 1
    h1 = list()
    for h in range(b):
        h = b%f ==0
        if h == True:
            h1.append(f)
        #print(h , " < > " , f)
        f += 1

    print(i1) #! delete
    print(h1) #! delete

    i2 = len(i1)
    h2 = len(h1)
    

    g = 0
    if i2 > h2:
        for y in range(h2):
            if i1[g] == h1[g]:
                print(i1[g] , "Дільник", a , b)
                g += 1
    if h2 > i2:
        for y in range(i2):
            if h1[g] == i1[g]:
                print(h1[g] , "Дільник", a , b)
                g += 1
    if i2 == h2:
            for y in range(h2):
                if i1[g] == h1[g]:
                    print(i1[g] , "Дільник", a , b)
                    g += 1
    return(a , b)

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

func (a , b)

print("\n - - Завдання 1.2 - -")

def runc(x , y):
    g = 1
    y1 = list()
    for i in range(6):
        y = x*g
        print("Число кратне" , x , "це число: ", y)
        y1.append(y)
        g += 1

x = int(input("Введіть ціле чсло: "))
print(x)
g = 1
y = x*g
y1 = list()
y1.append(y)
print(y1)
runc(x , y)