def conta_numero(numero,matriz):
    T=0
    for l in range(len(matriz)):
        for i in range(len(matriz[0])):
            if matriz[l][i]==numero:
                T+=1
    return T