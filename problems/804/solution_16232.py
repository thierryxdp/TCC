def filtra_pares(tupla):
    #tupla = (1, 2, 3, 4)
    aux = tupla
    if aux[3] % 2 != 0:
        aux.remove(aux[3])
    if aux[2] % 2 != 0:
        aux.remove(aux[2])
    if aux[1] % 2 != 0:
        aux.remove(aux[1])
    if aux[0] % 2 != 0:
        aux.remove(aux[0])        
    return tuple(aux)