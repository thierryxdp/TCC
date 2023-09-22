def eh_quadrada(matriz):
    '''função booleana que identifica se uma matriz é quadrada, bool->bool'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False