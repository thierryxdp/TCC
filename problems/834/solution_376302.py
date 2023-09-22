def media_matriz(m):
    cont = len(m)*len(m[0])
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma += m[i][j]
            
    return round(soma/cont,2)