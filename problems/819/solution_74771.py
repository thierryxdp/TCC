def filtraMultiplos(lista, n):
    """..."""
    lista = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            lista = lista + (t[proximo],)
        proximo = proximo + 1
    return lista