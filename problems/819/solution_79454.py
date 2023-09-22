def filtraMultiplos(lista, n):
    """..."""
    t = []
    x = 0
    while x < len(lista):
        if lista[x]%n == 0:
            list.append(t, lista[x])
        elif lista[x]%n != 0:
            None
        x = x + 2
    return t