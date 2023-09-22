def media_matriz(matriz):
    numerador = 0 
    denominador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador = numerador  + matriz[i][j]
            denominador = denominador + 1
    return round(numerador/denominador,2)