def media_matriz(m):
    soma=0
    peso=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma=soma+matriz[i][j]
            peso=peso+1
    return round(soma/peso,2)