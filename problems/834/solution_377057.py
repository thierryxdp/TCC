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
    for el in matriz:
        for el2 in el:
            soma+=el2
    return round((soma/quantidade),2)