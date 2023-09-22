def filtra_pares(x):
    'dada uma tupla de 4 elementos, retorna uma tupla contendo apenas os elementos pares da original tuple -> tuple'
    j=0
    while j<4:
        x1 = ()
        if x[j]/2 is int:
            x1=x1+x[j]
        j=j+1
    return x1