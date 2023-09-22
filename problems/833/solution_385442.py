def conta_numero(numero, matriz):
   #conta e retorna quantas vezes aquele um determinado número aparece na matriz
    indice = 0
    for i in range(0, len(matrizInt)):
        for counter in range(0, len(matrizInt[i])):
            if matrizInt[i][counter] == matrizNum:
                indice += 1

    return indice