def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada'''
    if len(matriz) == 0:
        return True
    else:
	    return len(matriz) == len(matriz[0])