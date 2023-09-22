def eh_quadrada(m):
    """calculo e retorno de uma funçao que identifica se uma matriz é quadrada."""
    if len(matriz)==0:
        return True
    for i in m:
        if len(m)==len(m[0]):
            return True
        else:
            return False