def eh_quadrada(m):
    """Essa função verifica se uma matriz e quadrada ou não
    lista->bool"""
    
    if len(m) == len(m[0]):
        return True
    else:
        return False