def media_matriz(m):
    soma=0
    qtd_numeros=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma += m[i][j]
            qtd_ numeros +=1
    return round(soma/qtd_numeros,2)