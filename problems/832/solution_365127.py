def eh_quadrada (y):
    '''função que identifica se uma matriz
    é quadrada ou não
    list->bool'''
    if y==[]:
        return True
    if len(y)== len(y[0]):
        return True
    else:
        return False