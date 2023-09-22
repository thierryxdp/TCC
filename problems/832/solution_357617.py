def eh_quadrada(matriz):
    '''Funcao que identifica se uma matriz e quadrada.
    list -> bool'''
    
    if len(matriz[0]) == len(matriz) or len(matriz) == 0:
        return True
    else:
        return False