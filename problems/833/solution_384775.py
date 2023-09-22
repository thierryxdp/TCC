def conta_numero(numero, matriz):
	 '''Função que dado um numero inteiro e uma matriz de numeros inteiros de tamanho qualquer, retorna quantas vezes o numero que foi dado aparece na matriz'''
	 ''' int, list -> int'''
	 qtd_de_vezes = 0 
	 for i in range(len(matriz)):
	 	for j in range(len(matriz[0])):
	 		quantas_vezes= list.count(matriz[0], numero)
	 	qtd_de_vezes += quantas_vezes
	 return qtd_de_vezes