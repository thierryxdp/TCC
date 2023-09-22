def conta_numero(numero, matriz):
	n = 0
	for i in matriz:
		for j in matriz:
			if matriz[i] ==numero:
				n = n +1
                i=i+1
	return n