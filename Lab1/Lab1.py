import math
while True:
    z=input("Czy chcesz wyjść z programu? T/N - wielkość litery nie ma znaczenia. ")
    if z=="T" or z=="t":
        break
    a=float(input("a "))
    b=float(input("b "))
    c=float(input("c "))
    delta=b**2-4*a*c
    if delta>0 and a!=0:
        x1=(-1*b+math.sqrt(delta))/(2*a)
        x2=(-1*b-math.sqrt(delta))/(2*a)
        print("Ten trójmian ma miejsca zerowe dla następujących x: ")
        print(x1)
        print(x2)
    elif delta==0 and a!=0:
        x=-1*b/2*a
        print("Ten trójmian ma jedno, podwójne miejsce zerowe dla x= ")
        print(x)
    elif a==0:
        x=-1*c/b
        print ("Nie jest to trójmian. Miejsce zerowe tej funkcji liniowej jest dla x= ")
        print (x)
    else:
        print ("Program nie obsługuje liczb zespolonych.")
        break