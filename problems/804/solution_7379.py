def filtra_pares(x,y,z,w):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    
    
    
    if int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[1]) % 2 != 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[3]) % 2 != ):
        return (int(filtra_pares[1]),int(filtra_pares[2]),int(filtra_pares[3]))
    elif int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[0]) % 2 != 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[2]),int(filtra_pares[3]))
    elif int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[0]) % 2 != 0 and int(filtra_pares[1]) % 2 != 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[1]),int(filtra_pares[3]))
    elif int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[1]) % 2 != 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[0]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[1]),int(filtra_pares[2]))
    
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[2]),int(filtra_pares[3]))
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[1]) % 2 != 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[1]),int(filtra_pares[3]))
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[1]) % 2 != 0:
        return (int(filtra_pares[1]),int(filtra_pares[2]))
    elif int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[0]) % 2 != 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[3]))
    elif int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[2]) % 2 != 0 and int(filtra_pares[0]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[2]))
    elif int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[0]) % 2 != 0 and int(filtra_pares[1]) % 2 != 0:
        return (int(filtra_pares[0]),int(filtra_pares[1]))
    
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[3]) % 2 != 0:
        return (int(filtra_pares[3]))
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[2]) % 2 != 0:
        return (int(filtra_pares[2]))
    elif int(filtra_pares[0]) % 2 == 0 and int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[1]) % 2 != 0:
        return (int(filtra_pares[1]))
    elif int(filtra_pares[1]) % 2 == 0 and int(filtra_pares[2]) % 2 == 0 and int(filtra_pares[3]) % 2 == 0 and int(filtra_pares[0]) % 2 != 0:
        return (int(filtra_pares[0]))
    
    else:
        return ()