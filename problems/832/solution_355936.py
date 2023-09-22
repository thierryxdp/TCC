def eh_quadrada(M):
    """ funcao recebe uma matriz e identifica se ela e quadrado ou nao
    entrada: int  saida: bool"""
    if len (M) == len(M[0]):
        return True
    elif M == [[]]:
        return True
    else:
        return False