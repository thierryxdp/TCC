def eh_quadrada(M):
    """Função que identifica se a matriz é ou não quadrada.
    list(list) - > bool"""
    if len(M)==0:
        return False
    elif len(M) == len(M[0]):
        return True
    else:
        return False