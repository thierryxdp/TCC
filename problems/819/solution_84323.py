def filtraMultiplos(lista,n):
    r=[]
    for x in lista:
        if x%n==0:
            r==r.append(x)
            return r