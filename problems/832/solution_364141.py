def eh_quadrada(M):
    """Função que identifica se uma matriz é quadrada ou não,
    e retorna um booleano;
    list, list -> bool"""
    if len(M) ==0:
        return True
    elif len(M) > 0 and len(M[0]) == len(M[-1]) and len(M) == len(M[0]):
            return True
    else:
        return False