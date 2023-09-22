def eh_quadrada(x):
    '''Recebe uma matriz e retorna se ela é quadrada; list->bool'''
    if not len(x)==len(x[0]):
        return False
    else:
        return True