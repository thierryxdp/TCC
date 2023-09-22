def filtra_pares(x,y,z,w):
    """Retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam"""
    """tuple -> tuple"""
    
    filtra_pares[0]= x
    filtra_pares[1]= y
    filtra_pares[2]= z
    filtra_pares[3]= w
    
    
    if int(x) % 2 == 0 and int(y) % 2 != 0 and int(z) % 2 != 0 and int(w) % 2 != 0:
        return (int(y),int(z),int(w))
    elif int(y) % 2 == 0 and int(x) % 2 != 0 and int(z) % 2 != 0 and int(w) % 2 != 0:
        return (int(x),int(z),int(w))
    elif int(z) % 2 == 0 and int(x) % 2 != 0 and int(y) % 2 != 0 and int(w) % 2 != 0:
        return (int(x),int(y),int(w))
    elif int(w) % 2 == 0 and int(y) % 2 != 0 and int(z) % 2 != 0 and int(x) % 2 != 0:
        return (int(x),int(y),int(z))
    
    elif int(x) % 2 == 0 and int(y) % 2 == 0 and int(z) % 2 != 0 and int(w) % 2 != 0:
        return (int(z),int(w))
    elif int(x) % 2 == 0 and int(z) % 2 == 0 and int(y) % 2 != 0 and int(w) % 2 != 0:
        return (int(y),int(w))
    elif int(x) % 2 == 0 and int(w) % 2 == 0 and int(z) % 2 != 0 and int(y) % 2 != 0:
        return (int(y),int(z))
    elif int(y) % 2 == 0 and int(z) % 2 == 0 and int(x) % 2 != 0 and int(w) % 2 != 0:
        return (int(x),int(w))
    elif int(y) % 2 == 0 and int(w) % 2 == 0 and int(z) % 2 != 0 and int(x) % 2 != 0:
        return (int(x),int(z))
    elif int(z) % 2 == 0 and int(w) % 2 == 0 and int(x) % 2 != 0 and int(y) % 2 != 0:
        return (int(x),int(y))
    
    elif int(x) % 2 == 0 and int(y) % 2 == 0 and int(z) % 2 == 0 and int(w) % 2 != 0:
        return (int(w))
    elif int(x) % 2 == 0 and int(y) % 2 == 0 and int(w) % 2 == 0 and int(z) % 2 != 0:
        return (int(z))
    elif int(x) % 2 == 0 and int(z) % 2 == 0 and int(w) % 2 == 0 and int(y) % 2 != 0:
        return (int(y))
    elif int(y) % 2 == 0 and int(z) % 2 == 0 and int(w) % 2 == 0 and int(x) % 2 != 0:
        return (int(x))
    
    else:
        return ()