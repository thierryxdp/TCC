def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada.
    list(list)-->bool'''
    if len(matriz) == 0:
    	return True
    if len(matriz) == len(matriz[0]):
        return True
    else :
        return False