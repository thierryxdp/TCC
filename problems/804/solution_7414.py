def filtra_pares(a,b,c,d):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    tuple = a,b,c,d

    
    if tuple[0] % 2 == 0 and tuple[1] % 2 != 0 and tuple[2] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[0]
    if tuple[1] % 2 == 0 and tuple[0] % 2 != 0 and tuple[2] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[1]
    if tuple[2] % 2 == 0 and tuple[0] % 2 != 0 and tuple[1] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[2]
    if tuple[3] % 2 == 0 and tuple[1] % 2 != 0 and tuple[2] % 2 != 0 and tuple[0] % 2 != 0:
        return tuple[3]
    
    if tuple[0] % 2 == 0 and tuple[1] % 2 == 0 and tuple[2] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[0], tuple[1]
    if tuple[1] % 2 == 0 and tuple[3] % 2 == 0 and tuple[1] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[1], tuple[3]
    if tuple[0] % 2 == 0 and tuple[3] % 2 == 0 and tuple[2] % 2 != 0 and tuple[1] % 2 != 0:
        return tuple[0], tuple[3]
    if tuple[1] % 2 == 0 and tuple[2] % 2 == 0 and tuple[0] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[1], tuple[2]
    if tuple[1] % 2 == 0 and tuple[3] % 2 == 0 and tuple[2] % 2 != 0 and tuple[0] % 2 != 0:
        return tuple[1], tuple[3]
    if tuple[2] % 2 == 0 and tuple[3] % 2 == 0 and tuple[0] % 2 != 0 and tuple[1] % 2 != 0:
        return tuple[2], tuple[3]
    if tuple[0] % 2 == 0 and tuple[2] % 2 == 0 and tuple[1] % 2 != 0 and tuple[3] % 2 != 0:
        return tuple[0], tuple[2]

    if tuple[0] % 2 == 0 and tuple[1] % 2 == 0 and tuple[2] % 2 == 0 and tuple[3] % 2 != 0:
        return tuple[0], tuple[1], tuple[2]
    if tuple[0] % 2 == 0 and tuple[1] % 2 == 0 and tuple[3] % 2 == 0 and tuple[2] % 2 != 0:
        return tuple[0], tuple[1], tuple[3]
    if tuple[0] % 2 == 0 and tuple[2] % 2 == 0 and tuple[3] % 2 == 0 and tuple[1] % 2 != 0:
        return tuple[0], tuple[2], tuple[3]
    if tuple[1] % 2 == 0 and tuple[2] % 2 == 0 and tuple[3] % 2 == 0 and tuple[0] % 2 != 0:
        return tuple[1], tuple[2], tuple[3]
    
    else:
        return ()