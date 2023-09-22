def fatorial(n):
    x=list(range(n))
    total=1
    y=1
    while y<(len(x)+1):
        total=total*x[y]
        y=y+1
    return total