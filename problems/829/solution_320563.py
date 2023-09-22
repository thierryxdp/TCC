def soma_h(n):
    s=0
    l=n+1
    for num in range(1,l):
        d=1/num
        s=s+d
        return round(s,2)