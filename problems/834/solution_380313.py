def media_matriz(m):
    media=0
    for i in range(len(m)):
        for j in range(len(m)):
            media+= m[i][j]
    return media