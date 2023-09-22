def media_matriz(matriz:list)->float:
    """ A função recebe com parâmetro de entrada uma matriz
    de inteiros não vazia, e retorna a média de todos os números
    da matriz. E essa média possui duas casas decimais"""
    soma = 0
    nlin = len(matriz)
    ncol = len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            soma += matriz [i][j]
    return soma