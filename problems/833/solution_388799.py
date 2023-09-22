def conta_numero(numero,matriz):
    a = 0
    for x in range(len(matriz)):
        for i in range(len(matriz[x-1])):
            if matriz[x-1][i-1] == numero:
                a = a+1
    return a