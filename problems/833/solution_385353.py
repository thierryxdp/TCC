def conta_numero(numero,matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == numero:
                total = total + 1
    return total