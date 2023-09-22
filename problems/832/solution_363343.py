def eh_quadrada(matriz):
    '''Retorna se a dada matriz é quadrada
    list -> bool'''
    return bool(len(matriz) == 0) or bool(len(matriz) == len(matriz[0]))