def soma_h(n):
    h = 0
    for e in range(n):
        h = h + 1/(n+1)
    return round(h, 2)