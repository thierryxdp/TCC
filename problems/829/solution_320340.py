def soma_h(N):
    H = 0
    for i in range(1,N+1):
        H+=1/i
    return round(H,2)