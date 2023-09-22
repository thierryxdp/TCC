def eh_quadrada (matriz):
    '''
    função que identidica e uma matriz é quadrada
    list->bool
    '''
    for x in matriz:
        if len(matriz) == len(matriz[0]) :
            return True   
        elif len(matriz) == len(matriz[0]) == 0:
            return True
        else:
            return False