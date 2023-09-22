def conta_numero(numero,matriz):
	""" Esta Função retorna a quantidade de vezes que um número X aparece na matriz 
	int,dict -> int """

	contador = 0
	for i in range(len(matriz)):
		if numero == matriz[i]:
			contador  += 1
		

	return contador