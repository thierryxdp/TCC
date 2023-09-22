def soma_h(n):
    i=0
    h=1
    while i<=n:
        h=h+(1/i)
        i=i+1
    return round(h,2)