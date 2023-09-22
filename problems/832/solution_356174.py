def eh_quadrada(m):
    """ a função recebe uma matriz e retorna FALSE se a matriz não for quadrada e TRUE caso seja;
    list->bool"""
    if m == []:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False