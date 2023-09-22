def conta_numero(n, matriz):
    contador = 0
    for i in matriz:
        for j in i:
            if (matriz[i][j] == n):
                contador +=1
    return contador