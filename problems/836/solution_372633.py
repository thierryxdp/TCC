def busca(a,mat):
    d=[]
    for i in range(len(mat)):
        if(mat[i][2]==a):
            d.append([mat[i][0],mat[i][1],mat[i][3]])

    return d