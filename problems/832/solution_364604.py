def eh_quadrada(x):
    'Define se uma matriz x é quadrada ou não'
    if len(x) == len(x[0]):
        return True
    else:
        return False
    if len(x)=="":
        return True