def eh_quadrada(lista):
    try:
    	if len(lista) == len(lista[0]):
        	return True
    	else:
        	return False
    except:
        return True