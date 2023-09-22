def media_matriz(m):
    """Recebe uma matriz e retorna a média de seus valores.
Testes: media_matriz([[1,1], [1,1], [1,1]]) == 1
media_matriz([[2,2,2], [2,2,2]]) == 2
Assinatura: mat --> int
"""
    lin = len(m)
    col = len(m[0])
    soma = 0
    vezes = 0
    for i in range(lin):
        for j in range(col):
            soma += m[i][j]
            vezes = vezes + 1
    return round(soma/vezes, 2)