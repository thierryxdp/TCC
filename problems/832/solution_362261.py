def eh_quadrada(m):
    '''
        Função que identifica se uma matriz é quadrada.
    '''
    if len(m)==0:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False