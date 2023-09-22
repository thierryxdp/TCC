def media_matriz(matriz):
    soma = 0
	for l in len(matriz):
        for n in len(matriz[l]):
            soma = soma + sum(matriz[l])
        media = soma / len(matriz)* len(matriz[0])
	return media