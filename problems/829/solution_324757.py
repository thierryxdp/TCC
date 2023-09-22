def soma_h(N):
    r=list(range(1,N+1))
    s=1
    for e in r:
        s=s+(1/e)
    return round(s-1,2)