def soma_h(N):
    H=1
    i=1
    for i in range(1, N+1):
        H=H+1/i
        i=i+1
    return round(H,2)-1