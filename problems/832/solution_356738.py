def eh_quadrada(listas):
    if listas == []:
        return True
    else:
    	linhas = len(listas)
    	colunas = len(listas[0])
        
    	if linhas == colunas:
        	return True
    	else:
        	return False