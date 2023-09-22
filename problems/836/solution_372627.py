def busca(a,mat):
    d=[]
    for i in range(len(mat)):
        if(a==mat[i][2]):
            d.append([a[i][0],a[i][1],a[i][3]])
    return d