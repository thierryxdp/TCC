def media_matriz(matriz):
    soma=0
    count =0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            count += 1
            x = soma/count
                
    return float(x,2)