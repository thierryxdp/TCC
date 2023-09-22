def filtra_pares(n):
    if n%2==0:
        return filter(filtra_pares,n)