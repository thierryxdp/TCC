def eh_quadrada (matriz):
    '''Identifica se a matriz é quadrada ou não, matriz->valor booleano'''
    if len(matriz) + 1 != len(matriz[0]) + 1:
        return False
    else:
        return True