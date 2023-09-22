def eh_quadrada(matriz):
    """
    	Identifica se a matriz inserida é quadrada
        list -> bool    	
    """
    if len(matriz)==len(matriz[0]) or matriz==[]:
        return True
    else:
        return False