def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    
    a, b, c, d = tup
    
    if a %2 == 0 and b %2 == 0 and c %2 == 0 and d %2 == 0:
        return a, b, c, d
    elif  a %2 == 0 and b %2 == 0 and c %2 == 0 and d %2 != 0:
        return a, b, c