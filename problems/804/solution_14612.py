def filtra_pares(tupla):
    x = tupla[0]%2
    y = tupla[1]%2
    z = tupla[2]%2
    w = tupla[3]%2
    
    pares = (tupla[0]%2 == 0), (tupla[1]%2 == 0), (tupla[2]%2 == 0), (tupla[3]%2 == 0)
    
    return pares