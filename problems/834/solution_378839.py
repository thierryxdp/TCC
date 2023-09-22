def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média
	de todos os números da matriz
    list -> float'''
    acumulador = 0
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            acumulador += matriz[i][j]
            contador += 1
	media = acumulador / contador
    return media