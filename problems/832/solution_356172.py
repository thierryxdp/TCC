def eh_quadrada(m):
    """ a função recebe uma matriz e retorna FALSE se a matriz não for quadrada e TRUE caso seja;
    list->bool"""
    if len(m) == len(m[0]) or m == []:
        return True
    else:
        return False