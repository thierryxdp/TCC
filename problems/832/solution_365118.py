def eh_quadrada (matriz):
    '''Identifica se a matriz é quadrada ou não, matriz->valor booleano'''
    if len(matriz) != len(matriz[0]):
        return False
    else:
        return True