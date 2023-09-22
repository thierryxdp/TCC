def eh_quadrada(M):
    """Identifica se uma matriz é quadrada ou não, retornando em valores booleanos
    lista --> boolean"""
    if len(M[0])==0:
        return True
    lin=len(M)
    col=len(M[0])
    elif lin==col:
        return True
    else:
        return False