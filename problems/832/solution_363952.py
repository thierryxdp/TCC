def eh_quadrada(x):
    ''' retorna se uma matriz é quadrada ou não.
    list(list) --> bool '''
    
    if x == list():
        return True
    
    y = len(x)
    z = len(x[0])
    
    return y == z