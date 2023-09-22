def media_matriz(matriz):

	soma = 0 #inicia contador em zero
	contador = 0 #inicia contador em zero
    
	for item in matriz:
		for item2 in item:
			soma += item2
			contador += 1
            
	media = soma/contador
    
	return round(media, 2)