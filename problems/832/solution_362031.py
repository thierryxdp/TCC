def eh_quadrada(m):
    """função que identifica se uma matriz é ou não quadrada. list->bool"""
    if len(m)==len(m[0]):
        return True
    elif len(m)==0:
        return True
    else:
        return False