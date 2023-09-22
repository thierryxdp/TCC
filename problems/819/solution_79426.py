def filtraMultiplos(lista, n):
    """..."""
    x = 0
    while n < len(lista):
        if lista[x]%n == 0:
            lista = lista + (lista[x])
        x = x + 1 
    return lista