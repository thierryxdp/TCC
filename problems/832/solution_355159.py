def eh_quadrada(m):

# retorna True se a matriz dada m for quadrada, false se não for quadrada e none se for vazia    
    	
    if m != []:
    	if len(m) == len(m[0]):
        	return True

    	else:
        	return False