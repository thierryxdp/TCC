def conta_numero(numero, matriz):
    n= 0
    for linha in matriz:
        for j in matriz:
            if n ==numero:
                n = n +1
    return n