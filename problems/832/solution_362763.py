def eh_quadrada(matriz):
	for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz == 0:
                return True
            if i == j:
                return True
            else:
                return False