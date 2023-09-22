def filtra_pares(tupl_orig):
    '''Retorna uma tupla apenas com os numeros pares
    da tupla original; Tuple (int,int,int,int) -> tuple'''
    tupl_nv = ()
    if ((tupl_orig[0]%2) == 0):
        tupl_nv += tupl_orig[0]
    elif ((tupl_orig[1]%2) == 0):
        tupl_nv += tupl_orig[1]
    elif ((tupl_orig[2]%2) == 0):
        tupl_nv += tupl_orig[2]
    elif ((tupl_orig[3]%2) == 0):
        tupl_nv += tupl_orig[3]
    return tupl_nv