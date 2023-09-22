# Função é quadrada:

def eh_quadrada(matriz):
	'''Dada uma matriz, retorna se ela é quadrada ou não.
	list(list) -> bool'''
	if len(matriz) == 0:
		return True
	if len(matriz) == len(matriz[0]):
		return True
	else:
		return False