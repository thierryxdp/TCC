def eh_quadrada(matriz):
    '''
    função que recebe uma matriz e 
    retorna um booleano dizendo se ela
    é quadrada ou não
    list -> bool
    '''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True 
    else:
        return False