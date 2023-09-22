def filtra_pares(a,b,c,d):
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    if not A:
        return (a)
    elif not B:
        return (a,b)
    elif not C:
        return (a,b,c)
    elif not D:
        return (a,b,c,d)