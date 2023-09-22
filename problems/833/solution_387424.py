def conta_numero(n, m):
    acumulas = 0
    i = 0
    for i in range(len(m)):
        
        for j in range(len(m[i])):
            if n == m[j][i]:
                acumulas = acumulas + 1
    return acumulas