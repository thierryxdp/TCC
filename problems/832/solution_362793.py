def eh_quadrada(matriz):
	i = range(len(matriz))
    j = range(len(matriz[i]))
    for n in matriz:
        if i!=j:
            return False
        else:
            i=i+1
            return True