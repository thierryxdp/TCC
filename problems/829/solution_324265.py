def soma_h(n):
    c = 0
    for i in range (1, n + 1):
        c += 1 / i
    return round(c, 2)