def filtraMultiplos(lista, n):
    """..."""
    x = 0
    while x < len(lista):
        if lista[x]%n == 0:
            list.append(lista, lista[x])
        elif lista[x]%n != 0:
            None
        x = x + 2
    return lista