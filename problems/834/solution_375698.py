def media_matriz(matriz):
    contador = 0
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            total += matriz[i][j]
            contador += 1
    return round(total/contador, 2)