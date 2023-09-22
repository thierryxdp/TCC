def conta_numero(numero,matriz):
	"""Tem como objetivo receber uma matriz e um número inteiro e retornar
qunatas vezes aquele número aparece na matriz"""
	#m = matriz[:]
	counter = 0
	for lista in matriz:
		for elem in lista:
			if elem == numero:
				counter +=1
	return counter