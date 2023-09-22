def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada
    entrada: list
    saída: bool
    '''
    if len(matriz)==0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False