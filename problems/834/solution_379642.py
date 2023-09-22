def media_matriz(mat):
    ls=[]
    l=len(mat)
    if mat == ls:
        return 0
    for i in range(l):
        for j in range(len(mat[0])):
            ls.append(mat[i][j])
    s=sum(ls)/len(mat[0])
    return round(s,2)