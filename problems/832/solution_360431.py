def eh_quadrada(M):
    """verifica se M eh uma matriz quadrada;
    list(list) -> bool"""
    if len(M)==len(M[0]):
        return True
    if len(M)==0:
        return True
    else:
        return False