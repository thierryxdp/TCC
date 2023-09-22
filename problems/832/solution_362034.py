def eh_quadrada(m):
    """função que identifica se uma matriz é ou não quadrada. list->bool"""
    if m==[]:
        return True
    elif len(m)==len(m[0]):
        return True
    else:
        return False