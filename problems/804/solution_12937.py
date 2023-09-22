def filtra_pares(x):
    """retorna"""
    if (x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and (x[3]%2 == 0):
        return x
    
    elif (x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and not (x[3]%2 == 0):
        return x[0], x[1], x[2]