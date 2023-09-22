def melhor_volta(matriz):
	tupla = []
	for i in range(len(matriz)):
   		for j in range(len(matriz[0])):
			if matriz[i][j] < 300:
                tupla = (i+1,matriz[i][j],j+1)
	return tupla