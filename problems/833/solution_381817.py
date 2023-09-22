def conta_numero(numero, matriz):
    count=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero== matriz[i][j]:
                count=count=1
    return count