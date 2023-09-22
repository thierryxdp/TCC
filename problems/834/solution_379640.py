def media_matriz(mat):
    ls=[]
    l=len(mat)
    if mat == ls:
        return 0
    for i in range(l):
        row=[]
        for j in range(len(mat[0])):
            row.append(round(mat[i][j]*1/2),2)
        ls.append(row)
    return ls