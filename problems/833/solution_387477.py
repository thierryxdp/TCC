def conta_numero(numero, matriz):
    '''Dado numero, retorna quantas vezes ele aparece na matriz.
    	int, list --> int'''
    cont = 0
    for x in matriz:
        for y in matriz:
            if matriz[x][y] == numero:
                cont = cont + 1
	return cont