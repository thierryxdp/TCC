def eh_quadrada(matriz):
    '''indetifica se é uma matriz quadrada. list(list)->boolean'''
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False