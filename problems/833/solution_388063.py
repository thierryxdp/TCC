def conta_numero(numero, matriz):
    '''conta quantas vezes um número aparece na matriz
    int, list -> int'''
    contador = 0
    for coluna in matriz:
        for linha in coluna:
            for valor in linha:
                if valor == numero:
                    contador += 1
	return contador