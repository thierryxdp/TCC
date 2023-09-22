def filtra_pares (a,b,c,d):
    x1 == a%2=0
    x2 == b%2=0
    x3 == c%2=0
    x4 == d%2=0
    if x1 == True:
        return a
    elif x1, x2 == True:
        return a, b
    elif x1, x2, x3 == True:
        return a, b, c
    elif x1, x2, x3, x4 == True:
        return a, b, c, d
    elif x2 == True:
        return b
    elif x2, x3 == True:
        return b, c
    elif x2, x3, x4 == True:
        return b, c, d
    elif x3 == True:
        return x3
    elif x3, x4 == True:
        return c, d
    elif x1, x3 == True:
        return a, c
    elif x1, x4 == True:
        return a, d