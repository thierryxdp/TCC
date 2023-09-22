def fatorial(num):
    a=list(range(num,-1,-1))
    total=1
    cont=0
    while cont<(int(len(a))-1):
        total=total*a[cont]
        cont=cont+1
    return total