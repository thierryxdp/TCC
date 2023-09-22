def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    linhas = len(matriz)
    for i in range(linhas):
        if linhas == 0:
            return True
        if linhas > 0:
    		if i in range(linhas):
            	colunas = len(matriz[0])
        		if j in range(colunas):
        			if linhas == colunas:
            			return True
            		else:
                		return False