def eh_quadrada(M):
    """Função booleana que identifica se uma matriz é quadrada """
    if len(M) == 0:
       return False
       linhas = len(M)
       colunas = len(M[0])
    return linhas == colunas