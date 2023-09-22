def eh_quadrada(M):
    """Função que identifica se uma matriz é quadrada ou não,
    e retorna um booleano;
    list, list -> bool"""
    while len(M[0]) == len(M[-1]):
        return True
    else:
        return False