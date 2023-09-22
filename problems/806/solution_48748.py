def PosNegZero(x):
	'''Função que verifica se um número x é positivo, negativo ou zero'''
	''' int --> str '''

	if x > 0:
		return str(x) + " e positivo"
	else:
		if x < 0:
			return str(X) + " e negativo"
		else:
			return str(x) + " e zero"