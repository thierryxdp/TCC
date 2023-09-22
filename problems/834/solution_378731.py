def media_matriz(m):
    return(round( sum(map(lambda x: x[0]*x[1],zip(m)))/sum(m),1))