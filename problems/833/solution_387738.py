def conta_numero(numero,matriz):
	""" Esta Função retorna a quantidade de vezes que um número X aparece na matriz 
	int,dict -> int """

	
	for i in range(len(matriz)):
		if numero in matriz[i]:
			x = matriz.count(numero)
	return x