def eh_quadrada(l):
    """Função que identifica se uma determinada matriz é quadrada.
    list -> bool
    """
    
    if len(l) == len(l[0]):
        return True
    else:
        return False