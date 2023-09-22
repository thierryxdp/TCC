def eh_quadrada(matriz):
    '''Funcao que identifica se uma matriz e quadrada.
    list -> bool'''
    
    if len(matriz) == 0 or len(matriz[0]) == len(matriz):
        return True
    else:
        return False