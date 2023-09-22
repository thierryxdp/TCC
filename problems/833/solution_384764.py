def conta_numero(matriz, n):
    total = 0
    for x in range(matriz):
        if x == n:
            total = total + 1
    return total