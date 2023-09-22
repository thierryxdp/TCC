def busca(se, mat):
    l = []
    for i in range(len(mat)):
        if mat[i][2] == se:
            l += mat[i][:2] + [mat[i][3]]
    return l