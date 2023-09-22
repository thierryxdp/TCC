def eh_quadrada(x):
    '''Recebe uma matriz e retorna se ela é quadrada; list->bool'''
    if x==[]:
        return True
    elif len(x)==len(x[0]):
        return True
    else:
        return False