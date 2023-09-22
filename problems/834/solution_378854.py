def media_matriz(mat):
    s = 0
    n = 0
    for i in range(len(mat)):
        for j in mat[i]:
            s += j
            n += 1
    med = s / n
    return round(med, 2)