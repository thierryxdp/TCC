def filtra_pares(x, y, z, w):
    """
    """
    valores = (x, y, z, w)
    pares = tuple(valores %2==0 )
    return pares