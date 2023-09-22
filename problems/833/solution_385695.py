def conta_numero(numero,matriz):
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                cont=cont+1
    return cont