def soma_h(N):
    H=0
    n=1
    while n<=N:
        H+=1/n
        n+=1
    return round(H,2)