def melhor_volta(matriz):
    ''' '''
    lista = 999999
    for i in range(len(matriz)):
        if min(matriz[i]) < 0:
        	lista = min(matriz[i])
	return lista