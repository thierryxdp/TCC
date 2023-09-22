def eh_quadrada(lista):
    """Identifica se uma matriz é quadrada
       list --> bool"""
    if len(lista[0]) == len(lista):
        return True
    else:
        return False