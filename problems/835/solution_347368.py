def melhor_volta(matriz):
    """Esta função recebe uma matriz 6 x 10 e retorna o menor valor da matriz, a linha em que está o menor valor e a coluna que está o menor valor
    lista -> float, float, float"""
	resultado = (0,float("inf"),0)
	for i in range(6):
		for j in range(10):
			if matriz[i][j] < resultado[1]:
				resultado = (i+1,matriz[i][j],j+1)
	return resultado