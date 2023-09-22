def filtraMultiplos(lista,n):
    mult=[]
    for x in lista:
        if x% n==0:
            mult.append(x)
    return mult