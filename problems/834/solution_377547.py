def media_matriz(matriz):
 
    for i in list(range(len(matriz))):
        soma = 0
        for j in list(range(len(matriz[0]))):
            soma = soma + matriz[i][j]
       	return soma