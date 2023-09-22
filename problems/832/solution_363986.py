def eh_quadrada(a):
    """ A função retorna se a matriz é quadrada
    	list -> bool """
    
    i = len(a)
    if i == 0:
        return True
    
    elif i == len(a[0]):
        return True