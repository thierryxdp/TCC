def media_matriz(m):
    media=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            media+= m[i][j]
            
    return media/len(m)*len(m[0])