def eh_quadrada(x):
    '''Dada uma matriz, identifica se ela é quadrada.
    list --> bool'''
    if x == [[]]:
        return True
    a = len(x)
    b = len(x[0])
    elif a == b:
        return True
    else:
        return False