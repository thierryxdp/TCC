def conta_numero(numero,matriz):
    vezes=0
    for i in range len(matriz):
        for j in range len(matriz[0]):
            if matriz[j][i]==numero:
                vezes=vezes+1
            else:
                pass
    return vezes