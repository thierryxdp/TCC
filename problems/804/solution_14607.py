def filtra_pares(tupla):
    x = tupla[0]%2
    y = tupla[1]%2
    z = tupla[2]%2
    w = tupla[3]%2
    
    return (x == True, y == True, z == True, w == True)