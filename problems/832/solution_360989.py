def eh_quadrada(matriz):
    """
    	Identifica se a matriz inserida é quadrada
        list -> bool    	
    """
    if matriz==[] or len(matriz)==len(matriz[0]):
        return True
    else:
        return False