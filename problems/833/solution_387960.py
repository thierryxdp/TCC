def conta_numero(numero,matriz):
	""" Esta Função retorna a quantidade de vezes que um número X aparece na matriz 
	int,dict -> int """

	contador = 0
    l = 0 
	for i in range(len(matriz[0])):
		if numero in matriz[i]:
			contador  += 1
		if contador < matriz[1].count(numero):
			contador += 1
		 

	return contador