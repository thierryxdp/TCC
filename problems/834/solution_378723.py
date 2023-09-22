def media_matriz(M):
    soma = 0
    qnt = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            soma = soma + M[i][j]
            qnt = qnt + 1
    return round(soma/qnt,2)