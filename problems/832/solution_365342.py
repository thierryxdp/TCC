def eh_quadrada(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != mat[j][i]:
                return False
    return True