def soma_h(n):
    h = 0

    for i in range(1, n):
        h += (1/i+1)
    return float (round (h,2))