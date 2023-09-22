from math import inf
def melhor_volta(matriz):
    placar = [inf]
	for i in range(len(matriz)):
   		for j in range(len(matriz[0])):
			if matriz[i][j] < placar:
                placar = (i+1,matriz[i][j],j+1)
	return placar