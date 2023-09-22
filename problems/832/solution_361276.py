def eh_quadrada(matriz):
    ''''Função que verifica se uma matriz dada é quadrada
    list -> bool'''
    if len(matriz) == len(matriz[0]):
    	return True
    else:
        return False