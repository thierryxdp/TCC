def eh_quadrada(matriz):
    '''funçao que identifica se a matriz é quadrada;list -> bool'''
    if len(matriz) > 0:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            False
    else:
        return True