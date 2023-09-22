def media_matriz(matriz):
    """Função que calcula a media numa matriz de inteiros."""
    """List -> Float"""
    soma = 0
    tamanho = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                soma += matriz[i][j]
                tamanho += 1
    return round(soma/tamanho,2)