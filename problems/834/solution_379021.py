def media_matriz(m):
    soma = 0
    qtd_numeros = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma+=m[i][j]
            qtd_numeros+=1
    return soma/qtd_numeros