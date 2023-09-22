def eh_quadrada(m):
    '''Identifica se uma matriz é quadrada.
    list->bool'''
    if len(m)==0:
        return True
    else:
        if len(m)==len(m[0]):
            return True
        else:
            return False