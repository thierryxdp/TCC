def conta_numero(n,matriz):
    x = 0
    for y in matriz:
        for k in y:
            if k == n:
                x = x + 1
    return x