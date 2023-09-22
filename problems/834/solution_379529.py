def media_matriz(matriz):
    soma = 0
    elementos = len(matriz)*len(matriz[0])
    for i in matriz:
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
	return elementos