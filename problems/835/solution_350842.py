import math

def melhor_volta(matriz):

 	resultado = (0,inf,0)

 	for l in range(6):
		for c in range(10):
			if matriz[l][c] < resultado[1]:
				resultado = (l+1,matriz[l][c],c+1)

 		return resultado