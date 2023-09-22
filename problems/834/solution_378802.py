def media_matriz(m):
    n=0
    l=[]
    for i in range(len(m)):
        for j in range (len(m[0])):
            	n=n+int(m[i][j])
                l=l+[m[i][j]]
    return n/len(l)