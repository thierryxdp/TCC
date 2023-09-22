def conta_numero(n, matriz):
    total = 0
    for x in range(1,matriz):
        if x == n:
            total = total + 1
    return total