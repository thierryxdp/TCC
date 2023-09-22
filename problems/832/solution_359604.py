def eh_quadrada(matriz):
    '''função que identifica se uma matriz é quadrada'''
    
    if matriz == []:
        return True
    
    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False