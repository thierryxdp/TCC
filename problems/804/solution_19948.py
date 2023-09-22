def filtra_pares (elem1,elem2,elem3,elem4):
    '''
       A função recebe 4 elementos inteiros e retorna 
       somente os inteiros que são pares
       tupla -> tupla
    '''
    pares = (elem1,elem2,elem3,elem4)
    if (elem1%2) != 0:
        pares = pares - elem1
    if (elem2%2) != 0:
        pares = pares - elem2
    if (elem3%2) != 0:
        pares = pares - elem3
    if (elem4%2) != 0:
        pares = pares - elem4
        return pares
    else:
        return ()