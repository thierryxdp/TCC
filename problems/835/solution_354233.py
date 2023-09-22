def melhor_volta(mat):
    """Função que recebe uma matriz 6x10, 6 voltas/corredores e 10 tempos, e retorna uma tupla com 
1) de quem foi a melhor volta da prova 2) qual foi o tempo dessa volta 3) e qual foi a volta.
signature: matrix --> tuple """
    tmp = 10000
    cor = 0
    vol = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] < tmp:
                tmp = mat[i][j]
                cor = i
                vol = j
    return (cor + 1, tmp, vol + 1)