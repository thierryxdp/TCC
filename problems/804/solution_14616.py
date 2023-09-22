def filtra_pares(tupla):
    x = (tupla[0]%2 == 0)
    y = (tupla[1]%2 == 0)
    z = (tupla[2]%2 == 0)
    w = (tupla[3]%2 == 0)
    
    if (x == True):
        pares = pares + tupla[0]
    elif (y == True):
        pares = pares + tupla[1]
    elif (z == True):
        pares = pares + tupla[2]
    elif (w == True):
        pares = pares + tupla[3]
    else:
        return pares