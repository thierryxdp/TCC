def media_matriz(m):
    y = 0
    for i in range(len(m)):
        for l in range(len(m[0])):
            y += m[i][l]
    return round(y/(len(m)*len(m[0])),2)