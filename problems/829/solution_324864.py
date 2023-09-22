def soma_h(N):
    x=0
    i=1
    while i in range(1,N+1):
        x=x+(1/i)
        i+=1
    return round(x,2)