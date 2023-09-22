def eh_quadrada(m):
    """ Retorna True caso m seja uma matriz quadrada e False caso contrário
    list -> bool"""
    if len(m) == len(m[0]):
        return True
    else:
        return False