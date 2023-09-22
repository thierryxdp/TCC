def conta_numero(numero,matriz):
    C=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                list.append(C,matriz[i][j])
    return len(C)