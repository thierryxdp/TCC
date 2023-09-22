def eh_quadrada(m):
    numeroLinhas=len(m)
    numeroColunas=len(m[0])
    if len(m)==0:
        return True 
    else:
        if numeroColunas==numeroLinhas:
        	return True
    	else:
        	return False