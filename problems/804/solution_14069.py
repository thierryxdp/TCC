def filtra_pares(x):
    if x%2==0:
        return list(filter(filtra_pares,x))