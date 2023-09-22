def filtra_pares (tuple):
    '''Retorna os elementos pares da tupla;
    int, int, int, int -> int'''
    return filter(tuple, int(tuple[0]%2 == 0)