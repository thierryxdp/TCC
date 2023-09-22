def filtra_pares (numeros):
    pares = []
    if numeros[0]%2==0:
        pares += numeros[0]
    else:
        return ()
        
    if  numeros[1]%2==0:
        pares += numeros[1]
    else:
        return ()
        
    if  numeros[2]%2==0:
        pares+=numeros[2]
    else:
        return ()
        
    if  numeros[3]%2==0:
        pares+= numeros[3]
    else:
        return ()
    return pares