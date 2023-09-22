def eh_quadrada(M):
    """Função que identifica se a matriz é ou não quadrada.
    list(list) - > bool"""
    if len(M) == len(M[00]):
        return True
    else:
        return False