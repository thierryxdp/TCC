def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    w = tupla[3]
    
    if (x%2 == 0):
        pares = x
    elif (y%2 == 0):
        pares = pares, y
    elif (z%2 == 0):
        pares = pares, z
    elif (w%2 == 0):
        pares = pares, w
    else:
        return pares