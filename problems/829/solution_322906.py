def soma_h(N):
    H = 1 + 1/N
    n = 2
    if N = 1:
        return 1
    while n < N:
        H = H + 1/n
        n = n + 1
    return round(H, 2)