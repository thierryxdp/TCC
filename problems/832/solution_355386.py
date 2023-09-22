def eh_quadrada(matriz):
    '''Retorna um valor booleano que identifica se uma matriz é quadrada ou não;
    list(list) -> bool'''
    if matriz == [[]] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False