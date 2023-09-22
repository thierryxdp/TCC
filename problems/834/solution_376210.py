def media_matriz(matriz):
    '''Dada uma matriz de entrada não vazia contendo inteiros , a função retorna a média de todos os números da matriz com exatamente duas casas decimais de precisão.
    list->float'''
    soma = 0
	for l in range(len(matriz)):
        soma = soma + sum(matriz[l])
    media = soma / (len(matriz)* len(matriz[0]))
	return round(media,2)