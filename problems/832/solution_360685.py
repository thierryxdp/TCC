def eh_quadrada(matriz):
    '''verifica se a matriz é quadrada
    list--> bool'''    
		
    if len(matriz) == 0:
    	return True
    
    for item in matriz:
    	if len(matriz) == len(item):
	        return True
        else:
			return False