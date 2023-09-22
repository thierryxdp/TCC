def media_matriz(matriz):
    '''A função recebe uma matriz de inteiros de entrada sucessivamente calcula e retorna a média de todos os números da matriz com exatamente
    duas casas de precisão. list-> float'''
    soma = 0
	for l in range(len(matriz)):
        soma = soma + sum(matriz[l])
    media = soma / (len(matriz)* len(matriz[0]))
	return round(media,2)