def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    
    a, b, c, d = tup
    
    if tup[0] %2 == 0:
        return tup[0]
    if tup[0] %2 == 0 and tup[1] %2 == 0:
        return tup[0], tup[1]