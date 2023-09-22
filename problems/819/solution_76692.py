def filtraMultiplos(lista, n):
    """ list, list->int"""
    i = 0
    nLista = []
    while i < len(lista):
        if lista[i] % n == 0:
            nLista.append(lista[i])

        i += 1

    return nLista