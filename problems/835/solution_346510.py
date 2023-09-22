def melhor_volta(matriz):
    ''' '''
    lista = 999999
    for i in range(len(matriz)):
        if min(matriz[i]) < 999999:
        	lista = min(matriz[i])
	return lista