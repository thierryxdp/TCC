def conta_numero(n, matriz):
    total = 0
    for x in matriz:
        if x == n:
            total = total + x
    return total