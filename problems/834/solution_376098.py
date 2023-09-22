def media_matriz(matriz):
	'''Calcula e retorna a média dos elementos de uma
    matriz não vazia'''
	soma = 0
	itens = 0
	for i in matriz:
		for j in i:
			soma += j
			itens += 1
	return round(soma/itens, 2)