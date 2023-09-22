def eh_quadrada(matriz):
    '''função que dada uma matriz, identifica se é quadrada ou
    não.  list->bool'''
    
    if len(matriz) == len(matriz[0]):
        return len(matriz) == len(matriz[0])