def media_matriz(matriz):
    " " "Dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;list, -> float " " "
    numerador = 0 
    denominador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador = numerador  + matriz[i][j]
            denominador = denominador + 1
    return round(numerador/denominador,2)