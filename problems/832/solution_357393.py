def eh_quadrada (M):
    """Funcao que retorna um dado booleano para identificar se uma matriz e quadrada ou nao"""
    linhas = len(M)
    colunas = len(M[])
    if (linhas) == (colunas) :
        return True
    else :
        return False