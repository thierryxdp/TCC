def media_matriz(m):
    b = len(m)*len(m[0])
    a = 0
    for i in m:
        for j in i:
            a += j
    return round(a/b, 2)