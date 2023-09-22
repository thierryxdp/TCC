def media_matriz(matriz):
    soma = 0
    for i in list(range(len(matriz))):
        soma2 = 0
        for j in list(range(len(matriz[0]))):
            soma2 = soma2 + matriz[i][j]
        soma = soma + soma2
  	return soma2