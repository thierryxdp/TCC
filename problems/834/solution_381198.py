def media_matriz(m):
    x = 0
    y = 0
    for i in range (len(m)):
        for j in m[i]:
            x += j
            j +=1
    return round(x,2)