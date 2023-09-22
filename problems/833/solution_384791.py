def conta_numero(n, matriz):
    total = 0
    for x in range(matriz+1):
        if x == n:
            total = total + 1
    return total