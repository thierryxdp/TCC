def conta_numero(numero, matriz):
    soma = 0
    for i in (range(len(matriz))):
        for j in range(len(matriz[i])):
            if numero in matriz[i]:
                soma += 1
            else:
                pass
    return soma