def filtra_pares (a, b, c, d):
    x1 = a%2==0
    x2 = b%2==0
    x3 = c%2==0
    x4 = d%2==0
    if x1 == True and x2 == True and x3 == True:
        return tuple (a, b, c)
    elif x4 == True:
        return d