def busca(s,mat):
    ls=[]
    for i in range(len(mat)):
        q=[]
        for j in range(len(mat[i])):
            if s == mat[i][j]:
                q.append(mat[i])
                del q[2]
            ls.append(q)
    return ls