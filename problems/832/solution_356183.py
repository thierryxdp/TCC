def eh_quadrada(matriz):
    '''Função identifica se uma dada matriz é quadrada ou não;
    list -> bool'''

    if matriz == [[]] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False