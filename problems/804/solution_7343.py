def filtra_pares(x,y,z,w):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    filtra_pares[1]= x
    filtra_pares[2]= y
    filtra_pares[3]= z
    filtra_pares[4]= w
    
    
 if  filtra_pares[1] % 2 = 0 and  filtra_pares[2] % 2 != 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[2], filtra_pares[3], filtra_pares[4])
    elif  filtra_pares[2] % 2 = 0 and  filtra_pares[1] % 2 != 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[3], filtra_pares[4])
    elif  filtra_pares[3] % 2 = 0 and  filtra_pares[1] % 2 != 0 and  filtra_pares[2] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[2], filtra_pares[4])
    elif  filtra_pares[4] % 2 = 0 and  filtra_pares[2] % 2 != 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[1] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[2], filtra_pares[3])
    
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[2] % 2 = 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[3], filtra_pares[4])
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[3] % 2 = 0 and  filtra_pares[2] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[2], filtra_pares[4])
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[2] % 2 != 0:
        return ( filtra_pares[2], filtra_pares[3])
    elif  filtra_pares[2] % 2 = 0 and  filtra_pares[3] % 2 = 0 and  filtra_pares[1] % 2 != 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[4])
    elif  filtra_pares[2] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[3] % 2 != 0 and  filtra_pares[1] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[3])
    elif  filtra_pares[3] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[1] % 2 != 0 and  filtra_pares[2] % 2 != 0:
        return ( filtra_pares[1], filtra_pares[2])
    
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[2] % 2 = 0 and  filtra_pares[3] % 2 = 0 and  filtra_pares[4] % 2 != 0:
        return ( filtra_pares[4])
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[2] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[3] % 2 != 0:
        return ( filtra_pares[3])
    elif  filtra_pares[1] % 2 = 0 and  filtra_pares[3] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[2] % 2 != 0:
        return ( filtra_pares[2])
    elif  filtra_pares[2] % 2 = 0 and  filtra_pares[3] % 2 = 0 and  filtra_pares[4] % 2 = 0 and  filtra_pares[1] % 2 != 0:
        return ( filtra_pares[1])
    
    else:
        return ()