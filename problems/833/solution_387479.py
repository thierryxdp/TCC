def conta_numero(numero, matriz):
    '''Dado numero, retorna quantas vezes ele aparece na matriz.
    	int, list --> int'''
    cont = 0
    for x in matriz:
        for y in matriz:
            if str(matriz[x][y]) == str(numero):
                cont = cont + 1
	return cont