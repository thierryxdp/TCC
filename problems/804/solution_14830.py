def filtra_pares(tup):
    """retorna os números pares de uma tupla"""
    
    if tup[0] % 2 == 0 and tup[1] % 2 == 0 and tup[2] % 2 == 0 and tup[3] % 2 == 0:
        return tup[0], tup[1], tup[2], tup[3] 
    elif tup[0] % 2 == 0 and tup[1] % 2 == 0 and tup[2] % 2 == 0 and tup[3] % 2 != 0:
        return tup[0], tup[1], tup[2]
    elif tup[0] % 2 == 0 and tup[1] % 2 != 0 and tup[2] % 2 == 0 and tup[3] % 2 != 0:
        return tup[0], tup[2]
    elif tup[0] % 2 == 0 and tup[1] % 2 == 0 and tup[2] % 2 != 0 and tup[3] % 2 != 0:
        return tup[0], tup[1]
    elif tup[0] % 2 != 0 and tup[1] % 2 != 0 and tup[2] % 2 != 0 and tup[3] % 2 == 0:
        return tup[3],
    elif tup[0] % 2 == 0 and tup[1] % 2 != 0 and tup[2] % 2 == 0 and tup[3] % 2 == 0:
        return tup[0], tup[2], tup[3]
    elif tup[0] % 2 != 0 and tup[1] % 2 != 0 and tup[2] % 2 == 0 and tup[3] % 2 == 0:
        return tup[2], tup[3]
    elif tup[0] % 2 != 0 and tup[1] % 2 == 0 and tup[2] % 2 == 0 and tup[3] % 2 != 0:
        return tup[1], tup[2]
    elif tup[0] % 2 != 0 and tup[1] % 2 == 0 and tup[2] % 2 == 0 and tup[3] % 2 == 0:
        return tup[1], tup[2], tup[3]
    else:
        return ()