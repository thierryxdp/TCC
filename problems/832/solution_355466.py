def eh_quadrada(matriz):
    """Dado de entreda uma matriz, retorna se é ou n quadrada"""
    """list=>bool"""
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
    	return True
    
    else:
        return False