def eh_quadrada(m):
    """Identifica se uma matriz é quadrada.
    list->bool"""
    check = True
    for i in range(len(m)):
        if len(m[i]) == len(m):
            check = True
        else:
            check = False
    return check