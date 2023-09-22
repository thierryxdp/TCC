def media_matriz(matriz):
    """
    lista-> float
    :param matriz: Recebe uma matriz de inteiros
    :param return: Retorna a medias desses nuemros em duas casas decimais
    """
    linhas=len(matriz)
    colunas=len(matriz[0])
    soma=0
    quantidade=linhas*colunas
    for linha in matriz:
        for coluna in linha:
            soma+=coluna
    return round((soma/quantidade),2)