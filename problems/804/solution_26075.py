def filtra_pares(a, b, c, d):
    if a%2==0:
        return tuple(a)
    else:
        if a%2==0 and b%2==0:
            return tuple(a,b)