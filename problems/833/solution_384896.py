def conta_numero(numero, matriz):
	count = 0
	for i in range(len(matriz)):
		for j in matriz[i]:
			if j == numero:
				count += 1
	return count