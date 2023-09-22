def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    nlin = len(matriz)
    ncol = len(matriz[0])
    soma = 0
    for i in matriz:
        for j in matriz:
            soma += matriz[i][j]
    return soma