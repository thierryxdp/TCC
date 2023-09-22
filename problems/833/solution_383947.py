def conta_numero(numero,matriz):
    contador=numero
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==0:
                contador+=1
    return contador