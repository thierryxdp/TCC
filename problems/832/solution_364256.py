def eh_quadrada (matriz):
    '''
    função que identidica e uma matriz é quadrada
    list->bool
    '''
    i=0
    for x in matriz:
        if len(matriz) == len(matriz[0]) :
            i=i+ x
            return True   
        else:
            return False