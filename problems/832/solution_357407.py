def eh_quadrada (M):
    """Funcao que retorna um dado booleano para identificar se uma matriz e quadrada ou nao"""
    linhas = len(M)
    colunas = len(M[0])
    if (linhas) == (colunas) :
        return True
    else :
        return False
    for i in range(colunas):
        return True