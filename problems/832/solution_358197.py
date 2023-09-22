def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada, ou seja, possui mesmo número
    de colunas e linhas
    lista -> bool'''
	if len(matriz) == len(matriz[0]) or len(matriz) == 0 and len(matriz[0]) == 0:
		return True
    else:
       	return False