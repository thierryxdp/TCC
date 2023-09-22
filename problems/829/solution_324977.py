def soma_h(n):
    i=1
    h=0
    while i<=n:
        h=h+(1/i)
        i=i+1
    return round(h,2)