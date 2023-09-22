def filtra_pares(x):
    t = ()
    for z in range(4):
        if  x[z]%2 == 0:
            aux=x[z]
            t = t + (aux,)
    return t