def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada'''
    if matriz == [[]]:
        return True
    else:
	    return len(matriz) == len(matriz[0])