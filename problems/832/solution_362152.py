def eh_quadrada(x):
    '''Recebe uma matriz e retorna se ela é quadrada; list->bool'''
    if len(x)==len(x[0]):
        return True
    else:
        return False