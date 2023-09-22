def conta_numero(numero,matriz):
    soma=0
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[0][j]==numero:
                soma=soma+1
    return soma