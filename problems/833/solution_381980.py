def conta_numero(numero,matriz):
    resultado=0
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            for matriz[i][j]== numero:
                resultado=resultado+1
    return resultado