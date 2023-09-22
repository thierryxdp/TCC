def media_matriz(matriz):
    soma = 0
    cont = 0
    for i in matriz:
        for j in i:
            soma += j
            cont += 1
	return soma/cont