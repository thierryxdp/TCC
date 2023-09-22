def media_matriz(matriz):
	soma = 0
	media = 0
	tamanho = len(matriz)*len(matriz[0])
	for l in range(len(matriz)):
		soma += sum(matriz[l])
	media = soma/tamanho
	return media