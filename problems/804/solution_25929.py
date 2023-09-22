def filtra_pares (tupla):
    '''Retorna os números pares da tupla, tuple -> tuple'''
    tupla = list (tupla)
    tupla = list (filter(lambda x: x%2==0, tupla))
    tupla = tuple (tupla)
    return tupla