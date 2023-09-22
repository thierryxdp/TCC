def eh_quadrada(x):
    'Define se uma matriz x é quadrada ou não'
    if len(x) == 0:
        return False
    elif len(x) == len(x[0]):
        return True

    else:
        return False