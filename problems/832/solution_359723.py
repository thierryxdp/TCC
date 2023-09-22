def eh_quadrada(m):
    """ funçao booleana que identifica se uma matriz é quadrada ou nao;list,list->bool"""
    return all(len(row) == len(m) for row in m)