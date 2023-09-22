def filtra_pares(x,y,z,w):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    
    filtra_pares[0]= (x,)
    filtra_pares[1]= (y,)
    filtra_pares[2]= (z,)
    filtra_pares[3]= (w,)
    
   
     if (x) % 2 = 0 and (y) % 2 != 0 and (z) % 2 != 0 and (w) % 2 != 0:
        return ((y),(z),(w))
    elif (y) % 2 = 0 and (x) % 2 != 0 and (z) % 2 != 0 and (w) % 2 != 0:
        return ((x),(z),(w))
    elif (z) % 2 = 0 and (x) % 2 != 0 and (y) % 2 != 0 and (w) % 2 != 0:
        return ((x),(y),(w))
    elif (w) % 2 = 0 and (y) % 2 != 0 and (z) % 2 != 0 and (x) % 2 != 0:
        return ((x),(y),(z))
    
    elif (x) % 2 = 0 and (y) % 2 = 0 and (z) % 2 != 0 and (w) % 2 != 0:
        return ((z),(w))
    elif (x) % 2 = 0 and (z) % 2 = 0 and (y) % 2 != 0 and (w) % 2 != 0:
        return ((y),(w))
    elif (x) % 2 = 0 and (w) % 2 = 0 and (z) % 2 != 0 and (y) % 2 != 0:
        return ((y),(z))
    elif (y) % 2 = 0 and (z) % 2 = 0 and (x) % 2 != 0 and (w) % 2 != 0:
        return ((x),(w))
    elif (y) % 2 = 0 and (w) % 2 = 0 and (z) % 2 != 0 and (x) % 2 != 0:
        return ((x),(z))
    elif (z) % 2 = 0 and (w) % 2 = 0 and (x) % 2 != 0 and (y) % 2 != 0:
        return ((x),(y))
    
    elif (x) % 2 = 0 and (y) % 2 = 0 and (z) % 2 = 0 and (w) % 2 != 0:
        return ((w))
    elif (x) % 2 = 0 and (y) % 2 = 0 and (w) % 2 = 0 and (z) % 2 != 0:
        return ((z))
    elif (x) % 2 = 0 and (z) % 2 = 0 and (w) % 2 = 0 and (y) % 2 != 0:
        return ((y))
    elif (y) % 2 = 0 and (z) % 2 = 0 and (w) % 2 = 0 and (x) % 2 != 0:
        return ((x))
    
    else:
        return ()