def media_matriz(mat):
    con = 0
    lis = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            lis = lis + [mat[i][j]]
            con += 1
    return round(sum(lis)/con, 2)