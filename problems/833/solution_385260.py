def conta_numero(numero, matriz):
    r = 0
    for i in matriz:
        for j in i:
            if j == numero:
                r = r + 1
    return r