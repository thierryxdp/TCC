def conta_numero(numero, matriz):
    conta = 0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            conta = conta + 1
    return conta