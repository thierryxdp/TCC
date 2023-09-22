def eh_quadrada(numero):
    '''Função para identificar se a matriz é quadrada, list -> bool'''
    for i in range(len(numero)):
        if i != 0:
    	    for j in range(len(numero[0])):
    	        if j == 0:
        	        return True
    	        elif i == j:
        	        return True
    	        else:
        	        return False
        else:
            return True