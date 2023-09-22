def filtraMultiplos(lista, n):
    """..."""
    t = ()
    x = 0
    while n < len(lista):
        if lista[x]%n == 0:
            t = t + (lista[x])
        x = x + 1 
    return lista