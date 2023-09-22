def filtra_pares(t): 

    pares = [1]
    cont = 1
    	
    if t[0] % 2 == 0:
        pares[cont] = t[0]
        cont = cont + 1
        
    elif t[1] % 2 == 0:
        pares[cont] = t[1]
        cont = cont + 1

    elif t[2] % 2 == 0:
        pares[cont] = t[2]
        cont = cont + 1

    elif t[3] % 2 == 0:
        pares[cont] = t[3]
        cont = cont + 1

    return tuple(pares)