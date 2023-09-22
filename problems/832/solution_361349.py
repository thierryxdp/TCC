def eh_quadrada(m):
    """Dada uma matriz m, identifica se a matriz é quadrada ou não
    list -> bool"""
    if len(m) == 0:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False