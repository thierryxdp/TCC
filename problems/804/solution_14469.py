def par(x):
    ''' retorna true se o numero x for par'''
    if x%2==0:
        return True
    else:
        return False
def filtra_pares(t):
    '''função que recebe uma tupla t que possui quatro parametros int e retorna uma tupla com apenas os parametros pares da tupla original'''
    return tuple(list(filter(par,z)))