def conta_numero(numero,matriz):
	contador=0
	for x in range(len(matriz)):
		for y in range(len(matriz[x])):
			if numero in matriz[y]:
				contador=contador+1
	return contador