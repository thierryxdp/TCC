def media_matriz(matriz):
    elen = []
    soma = 0
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            elen += [matriz[i][j]]
    for z in range(len(elen)):
        soma += elen[z]
    med = soma/len(elen)
    return round(med,2)