def eh_quadrada(matriz):
	if len(matriz) == 0:
		return True
	else:
		if len(matriz) == len(matriz[0]):
			return True
		else:
			return False

d1 = [[1, 2, 3], [4, 5, 6], [7,8,9]]
d2 = []