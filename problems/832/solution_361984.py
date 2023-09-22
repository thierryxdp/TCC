def eh_quadrada(matriz):
    """
    Retorna uma funcao booleana que verifica se uma matriz e quadrada ou
    nao; list->bool
    """
    if len(matriz) == 0:
        return True
    for i in range(0,len(matriz)):
    	if len(matriz[i]) == len(matriz):
        	return True
    	else:
        	return False