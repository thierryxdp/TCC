def filtraMultiplos(l,n):
    d=[]
    for numeros in l:
        if (numeros % n) == 0:
            d= d + [numeros,]
    return d