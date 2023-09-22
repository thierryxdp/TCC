def soma_h(n):
    s=0
    for num in range (1,n+1):
        d=1/num
        s=s+d
    return round(s,2)