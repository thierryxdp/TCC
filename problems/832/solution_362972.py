def eh_quadrada (matriz):
    '''
    	Função que informa se uma matriz é quadrada ou não. Sendo True para matriz quadrada e False para não quadrada
        list->bool
    '''
    if matriz == [] or len(matriz)==len(matriz[0]):
        return True
    else:
        return False