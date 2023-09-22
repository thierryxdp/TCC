def eh_quadrada(matriz):
    '''indentifica se uma matriz é quadrada
    list -> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) != len(matriz[0]):
        return False