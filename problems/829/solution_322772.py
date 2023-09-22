def soma_h(n):
    h = 0
    for x in range(1, n + 1):
        h = h + 1 / x
    return round(h, 2)