def conta_numeros(numero, matriz):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
     return contador