def conta_numero(matriz, n):
    total = 0
    for x in range(matriz+1):
        if x == n:
            total = total + 2
    return total