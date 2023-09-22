def melhor_volta(matriz):
	'''
	lista->tupla'''
	melhor_volta=0
	tempo=1000
	qual_volta=0
	for x in range(len(matriz)):
		for y in range(len(matriz[x])):
			if matriz[x][y]<tempo:
            	tempo=matriz[x][y]
                qual_volta=y
				melhor_volta=x
	return tuple(melhor_volta,tempo,qual_volta)