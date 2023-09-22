def media_matriz(matriz):
    '''Funcao que pega a matriz de entrada, e em seguida calcula sua média 
    list,list→int'''
    contador=0
    divisor= len(matriz)*len(matriz[0])
    for linha in range(len(matriz)):
		for coluna in range(len(matriz[linha])):
            contador+= matriz[linha][coluna]
	media= contador/divisor
    return round(media,2)