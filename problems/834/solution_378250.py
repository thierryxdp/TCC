def media_matriz(matriz):
    soma = 0
    divisor = 0 
    media = 0
    for linhas in matriz:
        for colunas in linhas:
            soma += colunas
            divisor += 1
	media = soma/divisor
   	return media