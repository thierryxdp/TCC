def soma_h(n):
    h=0.0
    for i in range(1,n+1):
        h = h+(1.0/i)
    return round(h,2)