def eh_quadrada(matriz):
    '''funçao que identifica se uma matriz é quadrada e retorna um valor booleano'''
    '''list(list) -> bool'''
    
     cont_i=len(matriz)
	    j=0
	    
	    while j < cont_i:
	        cont_j=len(matriz[j])
	        j=j+1
	        
	        if cont_i != cont_j:
	            return False
	        
	    if cont_i == cont_j:
	        return True