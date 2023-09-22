def filtra_pares([a,b,c,d]):
    if a%2==0 or b%2==0 or c%2==0 or d%2==0:
        return tuple(a,b,c,d)