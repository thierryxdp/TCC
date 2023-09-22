def eh_quadrada(x):
    '''Dada uma matriz, identifica se ela é quadrada.
    list --> bool'''
    a = len(x)
    b = len(x[0])
    c = [[]]
    if x == [[[]]]:
        return True
    elif a == b:
        return True
    else:
        return False