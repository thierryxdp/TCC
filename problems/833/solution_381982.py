def conta_numero(numero,matriz):
    resultado=0
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if matriz[i][j+1]==numero:
                resultado=resultado+1
    return resultado