def eh_quadrada(x):
    'Define se uma matriz x é quadrada ou não'
    if x == []:
        return True
    elif len(x) == len(x[0]):
        return True
    else:
        return False