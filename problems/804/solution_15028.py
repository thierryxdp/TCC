def filtra_pares(x, y, z, w):
    """
    """
    tupla = (x, y, z, w)
    pares = tuple(filter(tupla%2==0, x, y, z, w))
    return pares