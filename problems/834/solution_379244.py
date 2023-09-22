def media_matriz(matriz):
    soma = 0
    cont = 0
    for i in matriz:
        for j in matriz:
            soma += j
            cont += 1
	return soma/cont