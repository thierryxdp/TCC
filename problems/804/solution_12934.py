def filtra_pares(x):
    """retorna"""
    if (x[0]%2 == 0) and (x[1]%2 == 0):
        return x
    
    if (x[1]%2 == 0):
        return x[1]