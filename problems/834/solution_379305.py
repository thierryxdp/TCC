def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    tamanho = len(matriz)
    acumula = []
    for i in matriz:
        for j in matriz:
            acumula += matriz[i][j]
    return acumula