def conta_numero(numero, matriz):
	
	qtd_de_vezes = 0
	i = 0
	while i < len(matriz):
		qts = list.count(matriz[i], numero)
		qtd_de_vezes = qts
		i +=1
	return qtd_de_vezes