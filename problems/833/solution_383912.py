def conta_numero(numero,matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]%2==contador:
                contador+=1
    return contador