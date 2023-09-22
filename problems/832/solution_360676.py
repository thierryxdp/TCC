def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada
    list--> bool'''    

    for item in matriz:
    	if not matriz or len(matriz) == len(item):
	        return True
        else:
			return False