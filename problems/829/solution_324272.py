def soma_h(n):
    l=range(1,n+1)
    s=0
    x=0
    while x < len(l):
        s= s + round(1/l[x],2)
        x+=1
    return round(s,2)