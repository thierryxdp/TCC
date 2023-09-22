def soma_h(N):
    i=1
    s=0
    for i in range(N):
        if i<N:
            i=i+1
            s=s+ (1/i)
    return round(s,2)