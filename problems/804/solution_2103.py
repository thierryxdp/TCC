def filtra_pares(a,b,c,d):
    return sorted(filter(lambda x: x % 2 == 0, filtra_pares))