def faltante(lista):
    """..."""
    y = 0
    while lista[y] == y + 1:
        if lista[y] == y + 1:
            y = y + 1
            return y
        elif lista[0:-1] == y + 1:
            return lista[-1] + 1