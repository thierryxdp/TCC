def filtra_pares(a,b,c,d):
    if a%2 !=0:
        return b,c,d
    elif b%2 !=0:
        return a,c,d
    elif c%2 !=0:
        return a,b,d
    elif d%2 !=0:
        return a,b,c
    else:
        return a,b,c,d