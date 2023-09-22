def eh_quadrada(matriz):
    ''' Verifica se uma matriz é quadrada;
    	list -> bool
    '''
    
    if len(matriz) == 0:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    return False