def conta_numero(numero, matriz):
	 '''Função que dado um numero inteiro e uma matriz de numeros inteiros de tamanho qualquer, retorna quantas vezes o numero que foi dado aparece na matriz'''
	 ''' int, list -> int'''
	 qtd_de_vezes = 0 
	 for i in range(len(matriz)):
	 	if numero in matriz[i]:
	 		qtd_de_vezes += list.count(matriz[i], numero)
	 return qtd_de_vezes