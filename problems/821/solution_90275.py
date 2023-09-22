def fatorial(n):
    x=list(range(n))
    y=1
    while y<len(x):
        x[y+1]=x[y]*x[y+1]
    
    return x[y]