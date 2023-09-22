def conta_numero(n, m):
    """Recebe um número inteiro e uma matriz, e retorna a ocorrência desse
número dentro da matriz.
Testes: conta_numero(1, [[1,1], [1,1]]) == 4
conta_numero(2, [[1,1], [1,1]]) == 0
Assinatura: int, mat --> int
"""
    lin = len(m)
    col = len(m[0])
    vezes = 0
    if m == []:
        return vezes
    for i in range(lin):
        for j in range(col):
            if m[i][j] == n:
                vezes = vezes + 1
    return vezes