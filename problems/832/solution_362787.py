def eh_quadrada(matriz):
	i = len(matriz)
    j = range(len(matriz[0]))+1
    for n in matriz:
        if i!=j:
            return False
        else:
            return True