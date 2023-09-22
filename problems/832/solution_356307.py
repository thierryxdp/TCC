def eh_quadrada(matriz):
    ''' '''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) == len(matriz[0][0]):
        return False
    else:
        return False