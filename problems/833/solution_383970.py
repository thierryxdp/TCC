def conta_numero(numero,matriz):
    contador=0
    n=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==0:
                Contador=1
                n+=1
    return Contador