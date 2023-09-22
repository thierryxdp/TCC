def filtra_pares(x):
    """retorna"""
    if (x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and (x[3]%2 == 0):
        return x[0], x[1], x[2], x[3]
    
    elif (x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and not (x[3]%2 == 0):
        return x[0], x[1], x[2]
    
    elif not(x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and (x[3]%2 == 0):
        return x[1], x[2], x[3]
    
    elif (x[0]%2 == 0) and (x[1]%2 == 0) and not(x[2]%2 == 0) and (x[3]%2 == 0):
        return x[0], x[1], x[3]
    
    elif (x[0]%2 == 0) and not(x[1]%2 == 0) and (x[2]%2 == 0) and (x[3]%2 == 0):
        return x[0], x[2], x[3]
    
    elif (x[0]%2 == 0) and (x[1]%2 == 0) and not(x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[0], x[1]
    
    elif not(x[0]%2 == 0) and not(x[1]%2 == 0) and (x[2]%2 == 0) and (x[3]%2 == 0):
        return x[2], x[3]
    
    elif (x[0]%2 == 0) and not(x[1]%2 == 0) and not(x[2]%2 == 0) and (x[3]%2 == 0):
        return x[0],x[3]
    
    elif not(x[0]%2 == 0) and (x[1]%2 == 0) and (x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[1],x[2]
    
    elif (x[0]%2 == 0) and not(x[1]%2 == 0) and (x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[0], x[2]
    
    elif not(x[0]%2 == 0) and (x[1]%2 == 0) and not(x[2]%2 == 0) and (x[3]%2 == 0):
        return x[1], x[3]
    
    elif (x[0]%2 == 0) and not(x[1]%2 == 0) and not(x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[0],
    
    elif not(x[0]%2 == 0) and (x[1]%2 == 0) and not(x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[1],
    
    elif not(x[0]%2 == 0) and not(x[1]%2 == 0) and (x[2]%2 == 0) and not(x[3]%2 == 0):
        return x[2],
    
    elif not(x[0]%2 == 0) and not(x[1]%2 == 0) and not(x[2]%2 == 0) and (x[3]%2 == 0):
        return x[3],
    
    else:
        return ()