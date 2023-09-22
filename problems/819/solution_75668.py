def filtraMultiplos(lista, n):
    """ """
    lista1 = []
    indice = 0
    acumulador = 0
    while lista[indice] % n == 0:
        indice = indice + 1
        acumulador = acumulador + lista[indice]
    return lista1