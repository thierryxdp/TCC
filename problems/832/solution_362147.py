def simetrica(mat):
    for i, linha in enumerate(mat):
        if len(linha) != len(mat):
            return False
        for j in range(i):
            if linha[j] != mat[j][i]:
                return False
    return True