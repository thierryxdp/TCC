def eh_quadrada(matriz):
	'''Função recebe uma matriz e identifica se essa é uma matriz quadrada, caso seja, retorna True, caso não seja, retorna False'''
	'''list -> bool'''
	if len(matriz) == 0 or len(matriz) == len(matriz[0]):
		return True
	else:
		return False