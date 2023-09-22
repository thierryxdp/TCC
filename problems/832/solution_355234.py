def eh_quadrada(m):
    '''funcao que identifica se uma matriz 
    é quadrada; list -> bool'''
    
    if len(m)==0:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False