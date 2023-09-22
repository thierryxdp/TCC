def filtraMultiplos(lista, n):
    """..."""
    t = ()
    x = 0
    while n < len(lista):
        if t[x]%n == 0:
            lista = lista + (t[x])
            x = x + 1 
    return lista