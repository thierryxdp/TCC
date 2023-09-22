def eh_quadrada(matriz):
    nlin = len(matriz)
    ncolun = len(matriz[0])
    
    if ncolun == nlin or ncolun + nlin == 0:
    	return "true"
    else:
        return "false"