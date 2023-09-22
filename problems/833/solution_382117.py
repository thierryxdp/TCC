def conta_numero(numero,matriz):
	'''Dado um número inteiro e uma matriz de inteiros de entrada a função calcula e retorna quantas vezes esse número aparece na matriz.
    int,list->int'''
       qtd = 0
	for l in matriz:
		for n in l:
			if n == numero:
				qtd = qtd + 1
	return qtd