def eh_quadrada(matriz):
	'''Função que dada uma matriz identifica se ela é quadrada
	ou não, considerando que uma matriz quadrada possui número de
    linhas e colunas iguais e, que uma matriz vazia é quadrada.
	Entrada: lista de listas
	Saída: bool'''
	listavazia=[]
	if matriz==listavazia:
		return True
	elif len(matriz)==len(matriz[0]):
		return True
	else:
		return False