def filtra_pares(numeros):
    '''função que retorna uma tupla só com elementos pares.
        touple--> touple'''

    numeros_pares = ()
    
    if numeros[0] % 2 == 0:
        numeros_pares = numeros_pares + (numeros[0],)
    if numeros[1] % 2 == 0:
        numeros_pares = numeros_pares + (numeros[1],)
    if numeros[2] % 2 == 0:
        numeros_pares = numeros_pares + (numeros[2],)
    if numeros[3] % 2 == 0:
        numeros_pares = numeros_pares + (numeros[3],)
    
    return numeros_pares