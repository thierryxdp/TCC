def filtraMultiplos(lista):
    i = 0
    divisiveis = ()
    while i<len(lista):
        if lista[i]%2 == 0:
            divisiveis = divisiveis + lista[i]
        i = i + 1
    return divisiveis