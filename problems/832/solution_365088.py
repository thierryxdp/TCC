def eh_quadrada(matriz):
    '''funçao que identifica se uma matriz é quadrada;
    mat -> bool'''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False