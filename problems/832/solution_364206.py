def eh_quadrada(x):
    '''
    funcao booleana que identidica se uma matriz é quadrada
    list->bool
    '''
    if x==[]:
        return True 
    elif len(x)==len(x[0]):
        return True
    else:
        return False