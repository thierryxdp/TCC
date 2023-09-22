def eh_quadrada(M):
    """função que identifica se a matriz M é quadrada
    list -> bool"""
    return len(M) == 0 or len(M) == len(M[0])