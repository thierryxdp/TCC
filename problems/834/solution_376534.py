def media_matriz(matriz):
	'''Função que retorna a média de todos os numeros de uma matriz
	list->flout'''
    contador=0
	soma=0
	for x in range(len(matriz)):
		for y in range(len(matriz[x])):
			contador=contador+1
			soma=soma+matriz[x][y]
	media=round((soma/contador),2)
	return media