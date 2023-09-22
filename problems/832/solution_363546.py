def eh_quadrada(m):
    '''Retorna 'True' se a matriz dada é quadrada;
    list -> boolean'''
    
    if len(m) == 0 or len(m) == len(m[0]):
        return True
    else:
        return False