def media_matriz(m):
    n=0
    for i in range(len(m)):
        for j in range (len(m[0])):
            	n=n+int(m[i][j])
    return n/len(m)