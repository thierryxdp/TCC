def media_matriz(m):
    y = 0
    for i in range(len(m)):
        y += m[i][0]
    return y/(len(m)*len(m[0]))