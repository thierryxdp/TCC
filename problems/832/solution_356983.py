def eh_quadrada(matriz):
    """essa função, dada uma matriz, identifica se é quadrada ou não
	 utilizando uma função booleana True ou False, respectivamente
    list -> bool"""
    
    
    if matriz == []:
        return True
	elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False