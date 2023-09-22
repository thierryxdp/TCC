def eh_quadrada(v):
    "função que identifica se uma matriz é quadrada.list->bool."
    if len(v) != 0:
        if len(v) == len(v[0]):
            return True
        else:
            return False            
    else:
        return True