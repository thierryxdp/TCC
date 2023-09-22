def filtra_pares(tupla):
    x = tupla[0]
    y = tupla[1]
    z = tupla[2]
    z = tupla[3]
    
    pares = (0,0,0,0)
    
    if (x%2 == 0):
        pares[0] = x
    elif (y%2 == 0):
        pares[1] = y
    elif (z%2 == 0):
        pares[2] == z
    elif (w%2 == 0):
        pares[3] = w
    else:
        return pares [0], pares[1], pares[2], pares[3]