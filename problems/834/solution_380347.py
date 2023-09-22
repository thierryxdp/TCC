def media_matriz(matriz):
    ''' '''
    contador=0
    divisor= len(matriz)*len(matriz[0])
    for linha in range(len(matriz)):
		for coluna in range(len(matriz[linha])):
            contador+= matriz[linha][coluna]
	media= contador/divisor
    return media