def eh_quadrada(m):
    """Dada uma matriz, retorna True para matriz quadrada e False para 
    o contrário"""
    if len(m) == len(m[0]):
        return True
    else:
        retrun False