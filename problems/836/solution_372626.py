def busca(a,mat):
    d=[]
    for i in range(len(mat)):
        if(a==mat[i][2]):
            d.append([a[0],a[1],a[3]])
    return d