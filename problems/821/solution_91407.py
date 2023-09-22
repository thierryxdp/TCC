def fatorial(n):
    v=[]
    i=0
    x=1
    while n>0:
        v=v+[n,]
        n=n-1
    while i<len(v):
        x=x*v[i]
        i=i+1
    return x