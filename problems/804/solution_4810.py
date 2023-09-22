def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    
    a, b, c, d = tup
    
    if tup[0] %2 == 0:
        return tup[0]
    if tup[1] %2 == 0:
        return tup[1]
    if tup[2] %2 == 0:
        return tup[2]
    if tup[3] %2 == 0:
        return tup[3]
    elif tup[0] %2 == 0 + tup[1] %2 == 0:
        return tup[0] and tup[1]