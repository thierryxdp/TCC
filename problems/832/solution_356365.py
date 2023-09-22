def eh_quadrada(matriz):
    '''Dada uma matriz de entrada a função identifica-se essa matriz é quadrada. lista -> bool'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False