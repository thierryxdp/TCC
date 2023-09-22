def faltante(lista):
    """..."""
    y = 0
    while lista[y] == y + 1 or None:
        if lista[y] == y + 1:
            y = y + 1
            return y
        elif lista[y] == None:
            return (lista[-1] + 1)