def busca(s,mat):
    ls=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if s == mat[i][j]:
                ls.append(mat[i])
    for k in range(len(ls)):
        for l in range(len(ls[k])):
            if s in ls[k]:
                ls[k].remove(s)
    return ls