def soma_h(N):
    H=0
    n=1
    for n in range(1,N+1):
        H+=1/n
        n+=1
    return round(H,2)