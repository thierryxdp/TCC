def faltante(lista):
    """..."""
    y = 0
    while lista[y] == y + 1 or y + 2:
        if lista[y] == y + 1:
            y = y + 1
        elif lista[y] == y + 2:
            return y + 1