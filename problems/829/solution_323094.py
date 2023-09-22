def soma_h(N):
    H=0
    i=0
    for num in N:
        if i<=N:
            H=H+1/i
            i = i+1
    return round(H,2)