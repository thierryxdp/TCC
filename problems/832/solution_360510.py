def eh_quadrada(m):
    """função que recebe uma matriz e retorna se ela é ou não quadrada
	list -> bool"""
    
    lin = len(m)
    col = len(m[0])
    
    for i in m:
        if lin == col:
            return True
        else:
            return False
	
    return True