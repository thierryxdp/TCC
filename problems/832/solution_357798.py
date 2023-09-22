def eh_quadrada(matriz):
    """Esta função verifica se a matriz é quadrada
    list -> bool"""
    if matriz == []:
    	return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False