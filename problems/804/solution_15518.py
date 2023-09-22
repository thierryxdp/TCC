def filtra_pares(numeros):
    '''retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
    tuple -> tuple'''
    
    numeros = n1, n2, n3, n4
    pares = ()
    impares = ()
    if n1%2 == 0:
        pares = pares + (n1,)
    else:
        impares = impares + (n1,)
    if n2 % 2 == 0:
        pares = pares + (n2,)
    else:
        impares = impares + (n2,)
    if n3 % 2 == 0:
        pares = pares + (n3,)
    else:
        impares = impares + (n3,)
    if n4 % 2 == 0:
        pares = pares + (n4,)
    else:
        impares = impares + (n4,)             
    return pares