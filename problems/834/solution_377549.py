def media_matriz(matriz):
    soma = 0
 	for i in list(range(len(matriz))):
        for j in list(range(len(matriz[0]))):
            soma = soma + matriz[i][j]
    return soma