def soma_h(N):
    H = 1
    for i in range (2, N+1):
        H += 1/i
    return round(H, 2)