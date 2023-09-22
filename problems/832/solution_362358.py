def eh_quadrada(M):
    """Responde se a matriz é quadrada. (list->bool)"""
    if M==[] or len(M) == len(M[0]):
        return True
    else:
        return False