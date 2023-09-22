def eh_quadrada(matriz):
	''' Função que retorna se a matriz é quadrada ou não
	lista->bool'''
	if matriz == []:
		return True
	elif len(matriz) == len(matriz[0]):
		return True
	elif len(matriz)==0 :
		return True
	else:
		return False