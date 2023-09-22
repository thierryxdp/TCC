def soma_h(n):
    s=0
    for x in range(1,n+1):
        s+=(1/x)
    return round(s,2)