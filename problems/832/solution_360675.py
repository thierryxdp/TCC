def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada
    list--> bool'''
	
	matriz_vazia = []    

    for item in matriz:
    	if matriz == matriz_vazia or len(matriz) == len(item):
	        return True
        else:
			return False