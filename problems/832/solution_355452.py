def eh_quadrada(matriz):
    """ Retorna se a matriz e ou nao quadrada. list-->bool"""
    if matriz==[]:
    	return True
    else:
        if len(matriz)==len(matriz[0]):
    		return True
        if len(matriz)!=len(matriz[0]):
            return False