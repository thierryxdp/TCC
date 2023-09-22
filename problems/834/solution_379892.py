def media_matriz(mat):
    c = 0
    for linha in mat:
        for e in linha:
            c = c+1
    return c/len(mat[0])+len(mat)