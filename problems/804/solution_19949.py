def filtra_pares (elem1,elem2,elem3,elem4):
    '''
       A função recebe 4 elementos inteiros e retorna 
       somente os inteiros que são pares
       tupla -> tupla
    '''
    pares = (elem1,elem2,elem3,elem4)
    if (elem1%2) == 0 and (elem2%2) == 0 and (elem3%2) == 0 and (elem4%2) == 0:
        return pares
    elif (elem1%2) != 0 and (elem2%2) == 0 and (elem3%2) == 0 and (elem4%2) == 0:
        return pares - pares[0]
    elif (elem1%2) == 0 and (elem2%2) != 0 and (elem3%2) == 0 and (elem4%2) == 0:
        return pares - pares[1]
    elif (elem1%2) == 0 and (elem2%2) == 0 and (elem3%2) != 0 and (elem4%2) == 0:
        return pares - pares[2]
    elif (elem1%2) == 0 and (elem2%2) == 0 and (elem3%2) == 0 and (elem4%2) != 0:
        return pares - pares[3]
    else:
        return ()