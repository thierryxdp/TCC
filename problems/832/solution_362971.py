def eh_quadrada (matriz):
    '''
    	Função que informa se uma matriz é quadrada ou não. Sendo True para matriz quadrada e False para não quadrada
        list->bool
    '''
    if len(matriz)==len(matriz[0]) or matriz == []:
        return True
    else:
        return False