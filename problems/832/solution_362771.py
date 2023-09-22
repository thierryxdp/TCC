def eh_quadrada(matriz):
    i = 0
	for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            i=i+1
            if i==j:
                return True
            else: 
                return False