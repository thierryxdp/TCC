def busca(s,mat):
    ls=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if s == mat[i][j]:
                ls.append(mat[i])
                ls.remove(mat[i][j])
    return ls