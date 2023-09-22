def media_matriz(m):
    soma = 0
    elem_total= len(m) * len(m[0])
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma += m[i][j]
    
    return round(soma/elem_total,2)