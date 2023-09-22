def repetidos(lista):
    """..."""
    y = 1
    x = 0
    while y < len(lista):
        if lista[y] == lista[y-1]:
            x = x + 1
        else:
            None
        y = y + 1
    return x