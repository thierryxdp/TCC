def conta_numero(numero,matriz):
    contagem=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                contagem=contagem+1
    return contagem