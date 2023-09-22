def filtraMultiplos(lista, n):
    """ """
    lista1 = []
    for i in lista:
        if (i % n == 0):
            lista1.append(i)
    return lista1