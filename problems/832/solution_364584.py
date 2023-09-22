def eh_quadrada(matriz):
    """ Funçao que identifica se uma matriz é quadrada"""
    
    nlin=len(matriz)
    ncol=len(matriz[0])
    
    if len(matriz)==0 or nlin==ncol:
        return True
    else:
    	return False