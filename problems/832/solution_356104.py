def eh_quadrada(matriz):
    '''função que identifica se uma matriz de entrada é quadrada.
    list -> bool'''
    
    return matriz == [[]] or len(matriz) == len(matriz[0])