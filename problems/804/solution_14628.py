def filtra_pares(a,b,c,d):
    
    if (a%2 == 0):
        pares = a
    elif (b%2 == 0):
        pares = pares + b
    elif (c%2 == 0):
        pares = pares + c
    elif (d%2 == 0):
        pares = pares + d
    else:
        return (a,b,c,d)