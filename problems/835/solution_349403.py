from math import inf
def melhor_volta(matriz):
	placar = (0,inf,0)
	for i in range(len(matriz)):
   		for j in range(len(matriz[0])):
			if matriz[i][j] < inf:
                placar = (i+1,matriz[i][j],j+1)
	return placar