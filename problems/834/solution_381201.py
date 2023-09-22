def media_matriz(m):
    x = 0
    y = 0
    for i in range (len(m)):
        for j in m[i]:
            x += j
            y +=1
    return round(x/y,2)