def media_matriz(m):
    
    acumulas = 0
    i = 0
    for i in range(len(m)):
        
        for j in range(len(m[i])):
            if n == m[i][j]:
                acumulas = acumulas + [i]
    return acumulas