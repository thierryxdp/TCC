def eh_quadrada (x):
    """dado uma matriz no formato de matriz em python como parametro, a função diz se ela é ou não
    quadrada;
    list -> bool"""
    if len(x) == 0:
    	return True
    else:
        i = len(x)
    	j = len(x[0])
    	if i == j:
	    return True
   	else:
       	    return False