def conta_numero(numero, matriz):
    count = 0
    for m in matriz:
        for i in m:
            if numero == i:
                count += 1
    return count