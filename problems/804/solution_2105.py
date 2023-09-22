def filtra_pares(a,b,c,d):
    return sorted(filter(lambda (a,b,c,d): x % 2 == 0, filtra_pares))