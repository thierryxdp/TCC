def filtra_pares (x):
    ''' função que devolve apenas os números pares 
    tuple -> tuple
    '''
    if x[0:] % 2 == 0:
        return x[0:]
   
    else:
        return ()