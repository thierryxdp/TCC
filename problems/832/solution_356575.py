def eh_quadrada(m):
    "função que identifica se uma matriz é quadrada.list->bool."
    m =[[]]
    if len(m) != 0:
        if len(m) == len(m[0]):
            return True
        else:
            return False            
    else:
        return True