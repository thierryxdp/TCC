def busca(mat, se):
    l = []
    for i in range(len(mat)):
        if mat[i][2] == se:
            l += mat[i]
    return l