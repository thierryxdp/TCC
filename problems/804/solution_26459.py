def filtra_pares(numeros):
    pares = ()
    i = 0
    
    while (i < len(numeros)):
        if (numeros[i] % 2 == 0):
            pares = pares + (numeros[i],)
        i = i + 1
    
    return pares