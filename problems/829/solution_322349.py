def soma_h(N):
    y = 0
    for x in range(1, N):
        y = y + 1/x
    return round(y, 2)