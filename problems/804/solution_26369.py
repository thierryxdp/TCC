def filtra_pares(tup):
    x=[]
    for i in tup:
        if (i%2==0):
            x.append(i)
    return tuple(x)