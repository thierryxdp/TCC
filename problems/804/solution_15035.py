def filtra_pares(x, y, z, w):
    """
    """
    valores = (x, y, z, w)
    pares = tuple(filter(valores %2==0))
    return pares