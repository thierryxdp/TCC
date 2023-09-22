def media_matriz(matriz):
    '''calcula a média de todos os números da matriz
    list -> float'''
    soma = 0
    contador = 0
    for coluna in matriz:
        for numero in matriz:
            contador += 1
            soma += numero
	return soma/numero