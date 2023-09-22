def filtra_pares(tupla):
    x = tupla[0]%2
    y = tupla[1]%2
    z = tupla[2]%2
    w = tupla[3]%2
    
    return (x == 0, y == 0, z == 0, w == 0)