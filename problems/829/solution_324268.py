def soma_h(n):
    l=range(1,n+1)
    s=0
    for x in l:
        s= s + 1/l[x]
    return round(s,2)