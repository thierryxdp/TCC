def matriz_quadrada(m):
    '''
        Função que identifica se uma matriz é quadrada.
    '''
    if len(m) == len(m[0]):
        return 'A matriz é quadrada'
    else:
        return 'A matriz não é quadrada'