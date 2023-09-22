def eh_quadrada(matriz):
    '''indentifica se uma matriz é quadrada
    list -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) != len(matriz[0]):
        return False
    elif len(matriz) and len(matriz[0]) == 0:
        return True