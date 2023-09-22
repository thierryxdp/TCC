def eh_quadrada(x):
    """Função que identifica se a matriz é quadrada
    list --> bool"""
    if x==[]:
        return True
    elif len(x) == len(x[0]):
        return True
    else:
        return False