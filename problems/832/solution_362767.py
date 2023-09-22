def eh_quadrada(matriz):
	for i in range(len(matriz)+1):
        for j in range(len(matriz[i])+1):
            if i == j:
                return True
            else:
                return False