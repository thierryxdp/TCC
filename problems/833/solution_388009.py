def conta_numero(numero, matriz):
    cont = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if c == numero:
                cont += 1
    return cont