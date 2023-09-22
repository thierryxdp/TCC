def conta_numeros(n,m):
    r = 0
    for i in range(len(m)):
        for j in range(len(m[j][i])):
            if m[j][i] == n:
                r += 1
    return r