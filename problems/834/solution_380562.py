def media_matriz(matriz):
    somatorio = 0.0
    divisor = 0
    for i in matriz:
        for j in i:
            somatorio += matriz[i][j]
            divisor +=1
    resultado = somatorio / divisor
    return round(resultado, 2)