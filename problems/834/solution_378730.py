def media_matriz(m):
    return(round( sum(map(lambda x: x[0]*x[1],zip(A,B)))/sum(B),1))