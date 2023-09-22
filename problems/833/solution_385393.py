def conta_numero(numero,matriz):
    contagem=0
    for i range(len(matriz)):
        for j range(len(matriz[0])):
            if matriz[i][j]==numero:
                contagem +=1
    return contagem