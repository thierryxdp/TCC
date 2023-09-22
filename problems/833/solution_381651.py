def conta_numero(numero, matriz):
    c = 0
    for i in matriz:
        for j in range(len(i)):
            if i[j] == numero:
                c += 1
    return c