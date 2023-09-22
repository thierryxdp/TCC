def eh_quadrada(m):
    """retorna se a matriz é quadrada, lista -> bool"""
    if len(m) == 0:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False