def filtraMultipllos(lista,n):
    r=[]
    n=int
    for x in lista:
        if x%n==0:
            r=r+x
    return r