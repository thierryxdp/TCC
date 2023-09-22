def media_matriz(matriz):
    """Dada uma matriz como entrada, calcular e retornar a média de todos os números da matriz; list-> float"""
    linha = len(matriz)
    coluna = len(matriz[0])
    soma = 0
    n = linha*coluna
    for i in range(linha):
        for j in range(coluna):
            soma = soma + matriz[i][j]
    return soma/n