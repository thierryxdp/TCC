def eh_quadrada(matriz):
    '''Retorna um valor booleano que identifica se uma matriz é quadrada ou não;
    list(list) -> bool'''
    if matriz == []:
        return True
    if matriz != []:
    	if len(matriz) == len(matriz[0]):
        	return True
        if len(matriz) != len(matriz[0]):
            return False