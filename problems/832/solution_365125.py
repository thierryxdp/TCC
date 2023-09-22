def eh_quadrada (matriz):
    '''Função que descobre se a matriz é quadrada ou não
    matrix -> bool'''
    if len(matriz) != 0:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            return False
    return True