def filtra_pares(x,y,z,w):
    """função que retorna apenas as tuplas pares
    tuple, tuple, tuple, tuple -> tuple"""
    if (int(x%2==0)) and (int(y%2==0)) and (int(z%2==0)) and (int(w%2==0)):
        return (x,y,z,w)