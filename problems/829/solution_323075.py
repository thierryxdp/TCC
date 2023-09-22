def soma_h(N):
    i = 1
    H = 0
    while i <= N:
        H = H + (1/i)
        i = i + 1       
    return round(H,2)