def eh_quadrada(m):
    """Identifica se a matriz m é quadrada
    list->bool"""
    if m==[ ]:
        return True
    elif len(m)==len(m[0]):
        return True
    else:
        return False