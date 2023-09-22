def filtra_pares [(elem1,elem2,elem3,elem4)]:
    '''
       A função recebe 4 elementos inteiros e retorna 
       somente os inteiros que são pares
       tupla -> tupla
    '''
    pares = (elem1,elem2,elem3,elem4)
    if (elem1%2) != 0:
        pares = pares - pares[0]
    elif (elem2%2) != 0:
        pares = pares - pares [1]
    elif (elem3%2) != 0:
        pares = pares - pares [2]
    elif (elem4%2) != 0:
        pares = pares - pares [3]
        return pares
    else:
        return()