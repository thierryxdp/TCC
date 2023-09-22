def fatorial(n):
    x=list(range(n))
    total=1
    y=0
    while y+1<(len(x)):
        total=total*x[y]
        y=y+1
    return total