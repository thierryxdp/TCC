def media_matriz(matriz):
    soma = 0
    for i in matriz:
    	for j in range(len(matriz)):
            soma=soma+j
    return soma/len(matriz)