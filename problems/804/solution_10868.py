def filtra_pares(x,y,z,w):
    """função que retorna apenas as tuplas pares
    tuple, tuple, tuple, tuple -> tuple"""
    if (x%2==0) and (y%2==0) and (z%2==0) and (w%2==0):
        return (x,y,z,w)