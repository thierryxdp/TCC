# Função conta número

def conta_numero(matriz, n):
	'''Dada uma matriz de inteiros de qualquer tamanho e um número inteiro n, retorna a quantidade de vezes que n aparece na matriz.
	list(list), int -> int'''
	repeticoes = 0
	for linha in matriz:
		for aij in linha:
			if aij == n:
				repeticoes += 1
	return repeticoes