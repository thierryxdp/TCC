def eh_quadrada(matriz):
    '''
    Funçao que recebe uma matriz e diz se ela é quadrada
    list -> bool
    '''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False