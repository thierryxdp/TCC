def filtraMultiplos(lista,n):
    divisiveis = ()
    positivos = 0
    while positivos >= 0:
        if lista[0]/n:
            divisiveis = divisiveis + (lista[0],)
        positivos = positivos + 1
    return divisiveis