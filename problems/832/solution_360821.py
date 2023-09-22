def eh_quadrada(matriz):
    '''Recebe uma matriz,em lista, e retorna 
    se ele é uma matriz quadrada
    list->bool'''
    if matriz==[]:
        return True
    else:
        linha=len(matriz)
    	coluna=len(matriz[0])
    	if linha==coluna:
        	return True
    	else:
        	return False