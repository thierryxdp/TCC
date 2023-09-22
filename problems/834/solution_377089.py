def media_matriz(m):
    y = 0
    for i in range(len(m)):
        y += m[i][j]
    return y/(len(m)*len(m[0]))