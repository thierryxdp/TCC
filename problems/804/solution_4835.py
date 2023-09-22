def filtra_pares(tup):
    """Calcule e retorne os números pares de uma tupla"""
    
    a, b, c, d = tup
    
    if a %2 == 0:
        return a
    elif b %2 == 0:
        return b
    elif c %2 == 0:
        return c
    elif d %2 == 0:
        return d
    if a and b %2 == 0:
        return (a, b)