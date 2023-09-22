def filtra_pares(x,y,z,w):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    
    if filtra_pares[0] % 2 = 0 and filtra_pares[1] % 2 != 0 and filtra_pares[2] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[1],filtra_pares[2],filtra_pares[3])
    elif filtra_pares[1] % 2 = 0 and filtra_pares[0] % 2 != 0 and filtra_pares[2] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[0],filtra_pares[2],filtra_pares[3])
    elif filtra_pares[2] % 2 = 0 and filtra_pares[0] % 2 != 0 and filtra_pares[1] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[0],filtra_pares[1],filtra_pares[3])
    elif filtra_pares[3] % 2 = 0 and filtra_pares[1] % 2 != 0 and filtra_pares[2] % 2 != 0 and filtra_pares[0] % 2 != 0:
        return (filtra_pares[0],filtra_pares[1],filtra_pares[2])
    
    elif filtra_pares[0] % 2 = 0 and filtra_pares[1] % 2 = 0 and filtra_pares[2] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[2],filtra_pares[3])
    elif filtra_pares[0] % 2 = 0 and filtra_pares[2] % 2 = 0 and filtra_pares[1] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[1],filtra_pares[3])
    elif filtra_pares[0] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[2] % 2 != 0 and filtra_pares[1] % 2 != 0:
        return (filtra_pares[1],filtra_pares[2])
    elif filtra_pares[1] % 2 = 0 and filtra_pares[2] % 2 = 0 and filtra_pares[0] % 2 != 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[0],filtra_pares[3])
    elif filtra_pares[1] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[2] % 2 != 0 and filtra_pares[0] % 2 != 0:
        return (filtra_pares[0],filtra_pares[2])
    elif filtra_pares[2] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[0] % 2 != 0 and filtra_pares[1] % 2 != 0:
        return (filtra_pares[0],filtra_pares[1])
    
    elif filtra_pares[0] % 2 = 0 and filtra_pares[1] % 2 = 0 and filtra_pares[2] % 2 = 0 and filtra_pares[3] % 2 != 0:
        return (filtra_pares[3])
    elif filtra_pares[0] % 2 = 0 and filtra_pares[1] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[2] % 2 != 0:
        return (filtra_pares[2])
    elif filtra_pares[0] % 2 = 0 and filtra_pares[2] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[1] % 2 != 0:
        return (filtra_pares[1])
    elif filtra_pares[1] % 2 = 0 and filtra_pares[2] % 2 = 0 and filtra_pares[3] % 2 = 0 and filtra_pares[0] % 2 != 0:
        return (filtra_pares[0])
    
    else:
        return ()