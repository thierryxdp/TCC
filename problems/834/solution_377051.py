def media_matriz(M):
    total=0
    a=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            total+=1
            a+=M[i][j]
    return round(a/total,2)