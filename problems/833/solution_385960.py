def conta_numero(numero, matriz):
	n = 0
	for i in matriz:
		for j in matriz:
			if numero == matriz[i][j]:
				n = n + 1
           
	return n