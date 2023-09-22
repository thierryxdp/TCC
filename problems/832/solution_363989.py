def eh_quadrada(matriz):
    '''
    Essa função recebe uma matriz e retorna um bool dizendo se ela é quadrada
    
    list -> bool
    '''
    if len(matriz)==0:
    	return True
    elif len(matriz[0])==len(matriz):
        return True
    else:
        return False