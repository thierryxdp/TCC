def soma_h (N):
    ''''''
    H = 0
    for x in range(1,N+1):
        H += 1/x
    return round(H,2)