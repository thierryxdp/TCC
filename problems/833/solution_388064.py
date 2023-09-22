def conta_numero(numero, matriz):
    '''conta quantas vezes um número aparece na matriz
    int, list -> int'''
    contador = 0
    for coluna in matriz:
        for valor in coluna:
			if valor == numero:
				contador += 1
	return contador