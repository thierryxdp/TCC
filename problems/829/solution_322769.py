def soma_h(n):
    H = 0
    for x in range(1, n + 1):
        H = H + H / x
    return H