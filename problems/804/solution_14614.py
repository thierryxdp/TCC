def filtra_pares(tupla):
    x = (tupla[0]%2 == 0)
    y = (tupla[1]%2 == 0)
    z = (tupla[2]%2 == 0)
    w = (tupla[3]%2 == 0)
    
    return x == True, y == True, z == True, w == True