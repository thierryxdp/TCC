def soma_h(N):
    H = 0
    for i in range(0, N):
        H += 1 / (1 + i)
    
    return round(H, 2)