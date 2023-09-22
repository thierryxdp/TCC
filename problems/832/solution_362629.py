def eh_quadrada(matriz):
    '''
    dada uma matriz, verifica se ela é quadrada
    
    array -> bool
    '''
    
    output = bool(len(matriz) == len(matriz[0]))
    return output