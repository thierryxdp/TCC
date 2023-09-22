def filtra_pares(x):
    x = []
    for i in x:
        if i%2==0:
            x.append(i) 
            return tuple(x)