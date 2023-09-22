def eh_quadrada (M):
    """Funcao que retorna um dado booleano para identificar se uma matriz e quadrada ou nao"""
    if M==[]:
        return True
    elif (len(M)) == (len(M[0])) :
        return True
    else :
        return False