def conta_numero(matriz, n):
    total = 0
    for x in range(matriz+1):
        if n == x:
            total = total + 10
    return total