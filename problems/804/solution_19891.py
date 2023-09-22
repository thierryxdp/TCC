def filtra_pares (elem1,elem2,elem3,elem4):
    '''
       
       tupla, tupla, tupla, tupla -> tupla
    '''
    x = ((x%2) == 0)
    if ((elem1%2) == 0) and ((elem2%2) == 0) and ((elem3%2) == 0) and ((elem4%2) == 0):
        return (elem1, elem2, elem3, elem4)