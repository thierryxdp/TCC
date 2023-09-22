def media_matriz(matriz):
    '''Recebe uma matriz e calcula a sua media
    list -> float'''
    soma = 0 
	contador = 0 
	
    for item in matriz:
		for item2 in item:
			soma += item2
			contador += 1
	media = soma/contador
	return round(media, 2)