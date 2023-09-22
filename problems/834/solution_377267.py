def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz
    matriz -> float'''
    soma = 0
    for i in range(len(matriz)):
    	for j in range(len(matriz[i])):
       		soma += matriz[i][j]
        media = soma / (len(matriz) * len(matriz[0]))
		return round(soma,2)