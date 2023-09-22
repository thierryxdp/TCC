def media_matriz(matriz):
    """Essa função calcula a média (até duas casas decimais) dos elementos
    de uma matriz. Como entrada temos uma matriz e como saída temos a média;
    list->float"""
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
           soma+=matriz[i][j]
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)