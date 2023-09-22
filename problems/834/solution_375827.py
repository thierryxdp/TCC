def media_matriz(matriz):
    soma = 0
    for i in matriz:
    	for j in i:
            soma=soma+j
    return soma/(len(matriz)*len(matriz[0])