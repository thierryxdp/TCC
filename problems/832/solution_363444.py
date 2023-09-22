def eh_quadrada(m):
    ''' Essa função tem como objetivo verificar se uma matriz é quadrada'''
    '''list(list) -> bool'''
    
    if len(m) == 0:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False