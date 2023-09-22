def media_matriz(matriz):
    " " "Dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz;list, -> float " " "
    numerador = [] 
    denominador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador.append(matriz[i][j])
            denominador = denominador + 1
    resultado = map(lambda x:x/denominador,numerador))
    return round(resultado,2)