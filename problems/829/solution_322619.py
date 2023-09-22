def soma_h(n):
    l=list(range(1,n+1))
    r=1
    for i in l:
        r+=1/i
    return round(r,2)