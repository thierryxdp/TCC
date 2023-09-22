def media_matriz(matriz):
    '''calcula a média de todos os números da matriz
    list -> float'''
    soma = 0
    contador = 0
    for coluna in matriz:
        for numero in coluna:
            contador += 1
            soma += numero
	return round(soma/contador,2)