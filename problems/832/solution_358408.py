def eh_quadrada(matriz):
    """faça uma função para identificar se uma matriz é quadrada. Obs: uma matriz vazia é considerada quadrada
    list -> bool"""
    nlin = len(matriz)
    ncolun = len(matriz[0])
    
    if ncolun == nlin or ncolun + nlin == 0:
    	return True
    else:
        return False