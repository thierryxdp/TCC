def faltante(lista):
    """..."""
    y = 0
    if len(lista) == lista[-1]:
        return lista[-1] + 1
    else:
        while lista[y] == y + 1:
            y = y + 1
        return y