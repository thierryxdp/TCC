def eh_quadrada(m):
    '''
    A função retorna um valor booleano identificando se uma 
    matriz é quadrada ou não
    matriz --> bool
    '''
    if len(m) == len(m[0]) or len(m) == 0:
        return True
    else:
        return False