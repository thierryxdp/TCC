def conta_numero(numero, matriz):
    soma = 0
    for i in (range(len(matriz))):
        if numero in matriz[i]:
            soma += 1
        else:
            pass
    return soma