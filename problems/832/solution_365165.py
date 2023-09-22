def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j in matriz[i]:
        	if i==j or i==0:
                return True
            else:
                return False