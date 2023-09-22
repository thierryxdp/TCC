def eh_quadrada (m):
    """funcao que analisa se uma matriz m inserida e quadrada ou nao

       lista->bool
    """
    
    if len(m)==0:
        return True

    elif len(m) == len(m[0]):
        return True

    elif len(m) != len(m[0]):
        return False