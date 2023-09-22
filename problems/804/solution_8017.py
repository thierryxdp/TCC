def filtra_pares(numeros):
    pares = ()
    
    if numeros[0]%2==0:
        pares = pares + (numeros[0],)
    elif numeros[1]%2==0:
        pares = pares + (numeros[1],)
    elif numeros[2]%2==0:
        pares = pares + (numeros[2],)
    elif numeros[3]%2==0:
        pares = pares + (numeros[3],)

    return pares