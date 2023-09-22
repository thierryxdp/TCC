def melhor_volta(mat):
    x = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] < x:
                x = mat[i][j]
                c = i + 1
                v = j + 1
    return (c, x, v)