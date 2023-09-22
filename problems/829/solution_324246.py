def soma_h(n):
    h=0
    l=list(range(n+1))
    for x in l[1:]:
        h=h+(1/x)
    return round(h,2)