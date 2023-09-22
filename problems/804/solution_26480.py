def filtra_pares(tupla):
    pares = []
    for filtra in tupla:
        if(filtra % 2 == 0):
            pares.append(filtra)
            return tuple(pares)