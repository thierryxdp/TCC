def filtra_pares(x):
    if x%2==0:
        return lis(filter(filtra_pares,x))