def conta_numero(numero, matriz):
	count = 0
	for l in range(len(matriz)):
		for c in range(len(matriz[l])):
			if matriz[l][c] == numero:
				count+=1
	return count