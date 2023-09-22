def filtra_pares (elementos):
    '''
       A função recebe 4 elementos inteiros e retorna 
       somente os inteiros que são pares
       tupla -> tupla
    '''
    elem1, elem2, elem3, elem4 = elementos
    pares = tuple()
    if elem1%2 == 0:
        pares += (elem1, )
    if elem2%2 == 0:
        pares += (elem2, )
    if elem3%2 == 0:
        pares += (elem3, )
    if elem4%2 == 0:
        pares += (elem4, )
        return pares
    else:
        return pares