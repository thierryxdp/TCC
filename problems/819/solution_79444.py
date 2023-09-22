def filtraMultiplos(lista, n):
    """..."""
    t = ()
    x = 0
    j = 0
    while x < len(lista):
        if lista[x]%n == 0:
            list.append(t, lista[x])
            else:
                x = x + 1
        x = x + 1
    return t