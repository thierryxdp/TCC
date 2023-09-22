def filtraMultiplos(lista,n):
    r=[]
    for e in lista:
        if e%n==0:
            r=r+e
    return r