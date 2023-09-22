def conta_numero(numero, matriz):
    vezes = 0
    for i in matriz:
        for j in i:
            if numero == j:
                vezes += 1
    return vezes