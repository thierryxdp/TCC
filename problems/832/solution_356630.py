def eh_quadrada(M):
    """Identifica se uma matriz é quadrada ou não, retornando em valores booleanos
    lista --> boolean"""
    if M==[]:
        return True
    lin=len(M)-1
    col=len(M[0])-1
    elif lin==col:
        return True
    else:
        return False