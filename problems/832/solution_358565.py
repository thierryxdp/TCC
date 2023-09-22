def eh_quadrada(M):
    """Função que identifica se a matriz é ou não quadrada.
    list(list) - > bool"""
    if len(M) == len(M[0]) or len(M) == len(M[ ]):
        return True
    else:
        return False