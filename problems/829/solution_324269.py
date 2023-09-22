def soma_h(n):
    l=range(1,n+1)
    s=0
    for x in l:
        s= s + round(1/l[x],2)
    return round(s,2)