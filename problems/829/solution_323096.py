def soma_h(N):
    H=0
    i=0
    for i in range(0, N+1):
        H=H+1/i
        i=i+1
    return round(H,2)