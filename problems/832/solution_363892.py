def eh_quadrada (matriz):
    '''função que dada uma matriz retorna se é ou não
    uma matriz quadrada
    list->bool'''
    
    if matriz != []:
    	return len (matriz) == len (matriz[0])
    else:
        return True