def conta_numero(numero, matriz):
    c = 0
    for i in matriz:
        for j in i:
            if j == numero:
                c = c + 1
    return c