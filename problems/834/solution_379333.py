def media_matriz(M):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    nlin = len(M)
    ncol = len(M[0])

    multi = []
    for i in range(nlin):
        linha = []
        for j in range(ncol):
            linha += M[i][j]
        multi.append(linha)
    return multi