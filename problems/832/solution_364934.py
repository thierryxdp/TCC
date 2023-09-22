def eh_quadrada(m):
    '''função que identifica se uma matriz é quadrada ou não; list->bool'''
    if m == []:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False