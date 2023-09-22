def eh_quadrada(x):
    """essa função recebe uma matriz e define se ela é quadrada;
    int->bool"""
    if len(x) == 0:
        return True
    if len(x) == len(mat[0]):
        return True
    else:
        return False