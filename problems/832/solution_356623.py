def eh_quadrada(M):
    """Identifica se uma matriz é quadrada ou não, retornando em valores booleanos
    lista --> boolean"""
    lin=len(M)
    col=len(M[0])
    if M==[[]]:
        return True
    elif lin==col:
        return True
    else:
        return False