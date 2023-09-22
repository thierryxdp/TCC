def filtra_pares (elementos):
    '''
       A função recebe 4 elementos inteiros e retorna 
       somente os inteiros que são pares
       tupla -> tupla
    '''
    elem1,elem2,elem3,elem4 = elementos
    pares = tuple()
    if elem1%2 == 0:
        pares = + elem1
    elif elem2%2 == 0:
        pares = + elem2
    elif elem3%2 == 0:
        pares = + elem3
    elif elem4%2 == 0:
        pares = + elem4
        return pares