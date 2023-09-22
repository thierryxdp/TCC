def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    tamanho = len(matriz)
    soma = 0
    for i in matriz:
        for j in matriz:
            soma += int(matriz[i][j])
    return soma/tamanho