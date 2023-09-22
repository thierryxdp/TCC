def filtraMultiplos(lista, n):
    """..."""
    t = ()
    x = 0
    while x < len(lista):
        if lista[x]%n == 0:
            list.insert(t, -1, lista[x])
        x = x + 1 
    return t