def soma_h(n):
    a=0
    b=[]
    c=0
    for x in range(1,n+1):
        c=x**-1
        b.append(c)
    return round(sum(b),2)