def media_matriz(m):
    t=len(m[0])*len(m)
    d=0
    for i in range(len(m)):
        for n in range(len(m[0])):
            d=d+m[i][n]
    return round(d,2)