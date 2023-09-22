def eh_quadrada(m):
    """função que recebe uma matriz e retorna se ela é ou não quadrada
	list -> bool"""
    
    for i in m:
        if len(m) == len(m[0]):
            return True
        else:
            return False
	
    return True