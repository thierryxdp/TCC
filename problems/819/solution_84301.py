def filtraMultipllos(lista,n):
    r=[]
    for x in lista:
        if x%n==0:
            r=r+x
            return r